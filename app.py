"""
app.py  –  Vihara Tech AI Diabetes Prediction System
Flask backend v2 — with startup validation to detect stale/wrong pkl files.
"""
from flask import Flask, request, jsonify, render_template
import pickle, numpy as np, logging, os

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.FileHandler('main.log'), logging.StreamHandler()]
)

# ── Encodings — MUST match train_model.py exactly ────────────────────────────
PHYSICAL_MAP = {'Sedentary': 0, 'Light': 1, 'Moderate': 2, 'Active': 3}
SMOKING_MAP  = {'Never': 0, 'Former': 1, 'Current': 2}
CLASS_LABEL  = {0: 'Healthy', 1: 'Pre-Diabetic', 2: 'Diabetic'}
BMI_MEDIAN   = 28.1

# ── Expected scaler means (from training on diabetes_dataset.csv) ─────────────
# Used to detect if a stale/wrong scaler is loaded
EXPECTED_SCALER_MEANS = [
    0.41, 108.613, 100.719, 130.922, 5.708,
    48.614, 125.177, 28.190, 0.491, 1.251, 0.646
]

# ── Sanity-check samples: [features] -> expected_class_index ─────────────────
SANITY_CHECKS = [
    ([0, 107, 91, 119, 5.7, 32, 102, 27.7, 1, 1, 0], 0),   # Healthy
    ([0, 81, 168, 164, 5.1, 56, 134, 36.2, 1, 0, 0], 1),   # Pre-Diabetic
    ([1, 149, 50,  93,  6.7, 69, 118, 15.0, 0, 1, 0], 2),  # Diabetic
]

model  = None
scaler = None

def load_artifacts():
    global model, scaler
    # ── Load model ────────────────────────────────────────────────────────────
    try:
        with open('Model.pkl', 'rb') as f:
            model = pickle.load(f)
        logging.info("✅ Model loaded")
    except Exception as e:
        logging.error(f"❌ Model load failed: {e}")
        return False

    # ── Load scaler ───────────────────────────────────────────────────────────
    try:
        with open('standard_scaler (1).pkl', 'rb') as f:
            scaler = pickle.load(f)
        logging.info("✅ Scaler loaded")
    except Exception as e:
        logging.error(f"❌ Scaler load failed: {e}")
        return False

    # ── Validate scaler means (detect stale/mismatched pkl) ───────────────────
    actual_means = scaler.mean_
    for i, (expected, actual) in enumerate(zip(EXPECTED_SCALER_MEANS, actual_means)):
        if abs(expected - actual) > 1.0:
            logging.error(
                f"❌ STALE SCALER DETECTED at feature index {i}: "
                f"expected mean ~{expected:.3f}, got {actual:.3f}. "
                f"Please re-run train_model.py and replace Model.pkl + standard_scaler.pkl."
            )
            return False
    logging.info("✅ Scaler means validated")

    # ── Sanity-check predictions ───────────────────────────────────────────────
    all_ok = True
    for features, expected_class in SANITY_CHECKS:
        t = np.array([features], dtype=float)
        pred = model.predict(scaler.transform(t))[0]
        if int(pred) != expected_class:
            logging.error(
                f"❌ SANITY CHECK FAILED: features={features} "
                f"expected={CLASS_LABEL[expected_class]} got={CLASS_LABEL[int(pred)]}. "
                f"Model pkl is stale — re-run train_model.py."
            )
            all_ok = False
    if all_ok:
        logging.info("✅ All sanity checks passed — model predicts all 3 classes correctly")
    return all_ok

artifacts_ok = load_artifacts()
if not artifacts_ok:
    logging.critical(
        "🚨 STARTUP VALIDATION FAILED. "
        "Delete Model.pkl and standard_scaler.pkl, then re-run train_model.py"
    )

def _get(data, key, default=0):
    val = data.get(key, default)
    return val if val not in ('', None) else default


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        if not artifacts_ok or model is None or scaler is None:
            return jsonify({
                'error': (
                    'Model or scaler not loaded / validation failed. '
                    'Please run train_model.py and restart the server.'
                )
            }), 500

        data = request.get_json() if request.is_json else request.form
        logging.info(f"📥 Raw input: {dict(data)}")

        # ── Parse fields ──────────────────────────────────────────────────────
        family_history  = int(float(_get(data, 'family_history_diabetes_tri', 0)))
        glucose         = float(_get(data, 'glucose_mg_dlyeo_tri', 0))
        fasting_glucose = float(_get(data, 'fasting_glucose_mg_dlyeo_tri', 0))
        ogtt            = float(_get(data, 'ogtt_2hr_mg_dlyeo_tri', 0))
        hba1c           = float(_get(data, 'hba1c_pctyeo_tri', 0))
        age             = float(_get(data, 'age_CapMS', 0))
        sbp             = float(_get(data, 'sbp_mmhgyeo_CapMS', 0))
        bmi_raw         = _get(data, 'bmi_ranyeo_CapMS', '')
        bmi             = float(bmi_raw) if bmi_raw not in ('', None, 0, '0') else BMI_MEDIAN
        gender          = int(float(_get(data, 'gender_Male', 0)))
        phys_str        = _get(data, 'physical_activity_ordinal', 'Moderate')
        smok_str        = _get(data, 'smoking_status_ordinal', 'Never')

        physical = PHYSICAL_MAP.get(str(phys_str), 2)
        smoking  = SMOKING_MAP.get(str(smok_str), 0)

        # ── Feature vector (order matches train_model.py exactly) ─────────────
        features = np.array([[
            family_history,   # 0  family_history_diabetes
            glucose,          # 1  glucose_mg_dl
            fasting_glucose,  # 2  fasting_glucose_mg_dl
            ogtt,             # 3  ogtt_2hr_mg_dl
            hba1c,            # 4  hba1c_pct
            age,              # 5  age
            sbp,              # 6  sbp_mmhg
            bmi,              # 7  bmi
            gender,           # 8  gender_enc  (0=Female, 1=Male)
            physical,         # 9  physical_activity_enc
            smoking,          # 10 smoking_status_enc
        ]], dtype=float)

        logging.info(f"🔢 Feature vector: {features}")

        features_scaled = scaler.transform(features)
        pred  = int(model.predict(features_scaled)[0])
        proba = model.predict_proba(features_scaled)[0]

        classes = list(getattr(model, 'classes_', [0, 1, 2]))
        prob_dict = {
            CLASS_LABEL.get(int(c), str(c)): round(float(proba[i]) * 100, 2)
            for i, c in enumerate(classes)
        }

        result = {
            'prediction':  pred,
            'label':       CLASS_LABEL.get(pred, str(pred)),
            'probability': prob_dict,
        }
        logging.info(f"✅ Result: {result}")
        return jsonify(result)

    except Exception as e:
        logging.error(f"❌ Prediction error: {e}", exc_info=True)
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    logging.info(f"🚀 Starting on http://localhost:{port}")
    app.run(debug=True, host='0.0.0.0', port=port)