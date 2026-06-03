# ai-powered-diabetes-healthcare-system

python3 << 'PYEOF'
with open('/home/claude/photo_b64.txt') as f:
    photo_b64 = f.read().strip()

readme = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>AI-Powered Diabetes Prediction System — README</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:ital,wght@0,400;0,500;1,400&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0a0e17;
  --bg2:#0f1521;
  --bg3:#141b2d;
  --border:#1e2a42;
  --border2:#253350;
  --teal:#00c4b4;
  --teal2:#00e5d3;
  --teal-dim:rgba(0,196,180,.12);
  --teal-glow:rgba(0,196,180,.25);
  --gold:#f0a500;
  --gold2:#ffc843;
  --gold-dim:rgba(240,165,0,.12);
  --green:#22c55e;
  --green-dim:rgba(34,197,94,.1);
  --amber:#f59e0b;
  --amber-dim:rgba(245,158,11,.1);
  --red:#ef4444;
  --red-dim:rgba(239,68,68,.1);
  --blue:#3b82f6;
  --blue-dim:rgba(59,130,246,.1);
  --purple:#a855f7;
  --purple-dim:rgba(168,85,247,.1);
  --txt:#e2e8f0;
  --muted:#64748b;
  --muted2:#94a3b8;
  --sans:"DM Sans",sans-serif;
  --heading:"Syne",sans-serif;
  --mono:"DM Mono",monospace;
}
html{scroll-behavior:smooth;scrollbar-width:thin;scrollbar-color:var(--border) transparent}
body{font-family:var(--sans);background:var(--bg);color:var(--txt);min-height:100vh;line-height:1.7;font-size:15px}

/* ── Noise overlay ── */
body::before{content:"";position:fixed;inset:0;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");pointer-events:none;z-index:0;opacity:.4}
body>*{position:relative;z-index:1}

/* ── Grid lines ── */
.grid-bg{position:fixed;inset:0;background-image:linear-gradient(rgba(0,196,180,.03) 1px,transparent 1px),linear-gradient(90deg,rgba(0,196,180,.03) 1px,transparent 1px);background-size:40px 40px;pointer-events:none;z-index:0}

/* ── Top bar ── */
.topbar{background:rgba(10,14,23,.9);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);padding:0 48px;height:60px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100}
.tb-left{display:flex;align-items:center;gap:14px}
.tb-logo{display:flex;align-items:center;gap:8px}
.tb-logo-dot{width:8px;height:8px;border-radius:50%;background:var(--teal);box-shadow:0 0 10px var(--teal)}
.tb-logo-text{font-family:var(--heading);font-size:1.05rem;font-weight:700;color:#fff;letter-spacing:.02em}
.tb-sep{width:1px;height:20px;background:var(--border2)}
.tb-pill{font-family:var(--mono);font-size:.6rem;letter-spacing:.15em;text-transform:uppercase;color:var(--teal);background:var(--teal-dim);border:1px solid rgba(0,196,180,.2);border-radius:20px;padding:4px 12px}
.tb-right{display:flex;align-items:center;gap:10px}
.tb-tag{font-family:var(--mono);font-size:.58rem;color:var(--muted2);letter-spacing:.08em;text-transform:uppercase;padding:3px 10px;border:1px solid var(--border2);border-radius:6px}

/* ── Hero ── */
.hero{padding:80px 48px 64px;max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr auto;gap:60px;align-items:start}
.hero-eyebrow{display:inline-flex;align-items:center;gap:8px;font-family:var(--mono);font-size:.65rem;letter-spacing:.2em;text-transform:uppercase;color:var(--teal);margin-bottom:24px}
.hero-eyebrow-line{width:32px;height:1px;background:var(--teal);opacity:.5}
.hero h1{font-family:var(--heading);font-size:clamp(2.4rem,4.5vw,3.6rem);font-weight:800;line-height:1.08;color:#fff;margin-bottom:20px;letter-spacing:-.02em}
.hero h1 .hl{color:var(--teal);position:relative}
.hero h1 .hl::after{content:"";position:absolute;bottom:-3px;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--teal),transparent);border-radius:1px}
.hero-sub{font-size:.95rem;color:var(--muted2);max-width:520px;line-height:1.8;margin-bottom:32px}
.hero-chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:40px}
.chip{font-family:var(--mono);font-size:.62rem;letter-spacing:.08em;padding:5px 12px;border-radius:6px;border:1px solid;text-transform:uppercase;font-weight:500}
.chip.c-teal{color:var(--teal);border-color:rgba(0,196,180,.3);background:var(--teal-dim)}
.chip.c-gold{color:var(--gold2);border-color:rgba(255,200,67,.3);background:var(--gold-dim)}
.chip.c-green{color:var(--green);border-color:rgba(34,197,94,.3);background:var(--green-dim)}
.chip.c-blue{color:var(--blue);border-color:rgba(59,130,246,.3);background:var(--blue-dim)}
.chip.c-purple{color:var(--purple);border-color:rgba(168,85,247,.3);background:var(--purple-dim)}
.hero-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.hstat{background:var(--bg2);border:1px solid var(--border);border-radius:12px;padding:16px 14px;text-align:center;transition:border-color .2s}
.hstat:hover{border-color:var(--border2)}
.hstat-val{font-family:var(--heading);font-size:1.7rem;font-weight:800;line-height:1;margin-bottom:5px}
.hstat-val.t{color:var(--teal)}.hstat-val.g{color:var(--gold2)}.hstat-val.gr{color:var(--green)}.hstat-val.b{color:var(--blue)}
.hstat-lbl{font-size:.65rem;font-family:var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}

/* Profile card */
.profile-card{background:var(--bg2);border:1px solid var(--border);border-radius:20px;padding:28px 22px;text-align:center;width:200px;flex-shrink:0;position:relative;overflow:hidden}
.profile-card::before{content:"";position:absolute;top:-40px;left:50%;transform:translateX(-50%);width:160px;height:160px;background:radial-gradient(circle,var(--teal-glow),transparent 70%);pointer-events:none}
.profile-ring{width:110px;height:110px;margin:0 auto 16px;border-radius:50%;padding:2.5px;background:conic-gradient(var(--teal),var(--teal2),var(--gold),var(--teal));position:relative;z-index:1}
.profile-img-inner{width:100%;height:100%;border-radius:50%;overflow:hidden;background:var(--bg3)}
.profile-img-inner img{width:100%;height:100%;object-fit:cover;object-position:top center;display:block}
.p-name{font-family:var(--heading);font-size:.95rem;font-weight:700;color:#fff;margin-bottom:3px}
.p-role{font-family:var(--mono);font-size:.57rem;letter-spacing:.14em;text-transform:uppercase;color:var(--teal);margin-bottom:14px}
.p-div{width:32px;height:1px;background:var(--border2);margin:0 auto 12px}
.p-skills{display:flex;flex-wrap:wrap;gap:5px;justify-content:center}
.p-skill{font-family:var(--mono);font-size:.54rem;padding:3px 8px;border-radius:4px;background:var(--bg3);border:1px solid var(--border);color:var(--muted2);letter-spacing:.04em}

/* ── Content ── */
.content{max-width:1100px;margin:0 auto;padding:0 48px 80px}

/* Section headers */
.sec-head{display:flex;align-items:center;gap:12px;margin:56px 0 24px}
.sec-num{font-family:var(--mono);font-size:.62rem;color:var(--teal);letter-spacing:.1em;opacity:.6;min-width:24px}
.sec-title{font-family:var(--heading);font-size:1.25rem;font-weight:700;color:#fff;letter-spacing:-.01em}
.sec-line{flex:1;height:1px;background:linear-gradient(90deg,var(--border2),transparent)}

/* Cards */
.card{background:var(--bg2);border:1px solid var(--border);border-radius:16px;padding:28px;margin-bottom:16px;transition:border-color .2s}
.card:hover{border-color:var(--border2)}

/* ── Pipeline ── */
.pipeline{display:grid;grid-template-columns:repeat(6,1fr);gap:0;margin-bottom:16px;position:relative}
.pipeline::before{content:"";position:absolute;top:32px;left:10%;right:10%;height:1px;background:linear-gradient(90deg,transparent,var(--teal),var(--teal),var(--teal),transparent);opacity:.2;z-index:0}
.pipe-step{text-align:center;padding:20px 10px;position:relative;z-index:1}
.pipe-icon{width:64px;height:64px;border-radius:14px;margin:0 auto 12px;display:flex;align-items:center;justify-content:center;font-size:1.5rem;border:1px solid;position:relative}
.pipe-icon::after{content:"";position:absolute;inset:0;border-radius:14px;opacity:.12}
.pi-1{border-color:rgba(59,130,246,.4);background:rgba(59,130,246,.08)}
.pi-2{border-color:rgba(168,85,247,.4);background:rgba(168,85,247,.08)}
.pi-3{border-color:rgba(245,158,11,.4);background:rgba(245,158,11,.08)}
.pi-4{border-color:rgba(0,196,180,.4);background:rgba(0,196,180,.08)}
.pi-5{border-color:rgba(34,197,94,.4);background:rgba(34,197,94,.08)}
.pi-6{border-color:rgba(240,165,0,.4);background:rgba(240,165,0,.08)}
.pipe-label{font-family:var(--mono);font-size:.58rem;letter-spacing:.07em;text-transform:uppercase;color:var(--muted2);line-height:1.4}
.pipe-sub{font-size:.65rem;color:var(--muted);margin-top:3px}
.pipe-arrow{position:absolute;right:-8px;top:28px;color:var(--border2);font-size:.8rem;z-index:2}

/* ── Feature grid ── */
.feat-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:16px}
.feat-card{background:var(--bg3);border:1px solid var(--border);border-radius:12px;padding:20px 18px;transition:all .2s}
.feat-card:hover{border-color:var(--border2);transform:translateY(-2px)}
.feat-icon{font-size:1.4rem;margin-bottom:10px}
.feat-name{font-family:var(--heading);font-size:.85rem;font-weight:700;color:#fff;margin-bottom:5px}
.feat-desc{font-size:.75rem;color:var(--muted2);line-height:1.6}

/* ── Dataset table ── */
.dtable{width:100%;border-collapse:collapse;font-size:.8rem}
.dtable th{font-family:var(--mono);font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);padding:10px 14px;border-bottom:1px solid var(--border);text-align:left;font-weight:500}
.dtable td{padding:10px 14px;border-bottom:1px solid rgba(30,42,66,.5);color:var(--muted2);vertical-align:top}
.dtable tr:hover td{background:rgba(255,255,255,.02)}
.dtable tr:last-child td{border-bottom:none}
.dtable .col-name{font-family:var(--mono);font-size:.72rem;color:var(--teal);font-weight:500}
.dtable .col-type{font-family:var(--mono);font-size:.62rem;color:var(--muted);background:var(--bg3);border:1px solid var(--border);border-radius:4px;padding:1px 7px;display:inline-block}
.dtable .col-use{display:inline-block;font-size:.6rem;font-family:var(--mono);padding:2px 8px;border-radius:4px;letter-spacing:.05em}
.col-use.used{background:var(--teal-dim);color:var(--teal);border:1px solid rgba(0,196,180,.2)}
.col-use.derived{background:var(--gold-dim);color:var(--gold2);border:1px solid rgba(255,200,67,.2)}
.col-use.dropped{background:rgba(100,116,139,.08);color:var(--muted);border:1px solid var(--border)}

/* ── Model comparison ── */
.models-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:16px}
.model-card{background:var(--bg3);border:1px solid var(--border);border-radius:12px;padding:18px 16px;text-align:center;transition:all .2s;position:relative;overflow:hidden}
.model-card.best{border-color:rgba(0,196,180,.4);background:linear-gradient(145deg,rgba(0,196,180,.06),var(--bg3))}
.model-card.best::before{content:"FINAL MODEL";position:absolute;top:8px;right:-18px;font-family:var(--mono);font-size:.48rem;letter-spacing:.1em;background:var(--teal);color:#000;padding:3px 24px;transform:rotate(45deg);font-weight:600}
.model-icon{font-size:1.5rem;margin-bottom:8px}
.model-name{font-family:var(--heading);font-size:.8rem;font-weight:700;color:#fff;margin-bottom:8px}
.model-acc{font-family:var(--heading);font-size:1.6rem;font-weight:800;margin-bottom:3px}
.model-acc.best-acc{color:var(--teal)}
.model-acc.ok{color:var(--muted2)}
.model-lbl{font-family:var(--mono);font-size:.55rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}

/* ── Class breakdown ── */
.class-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.class-card{border-radius:14px;padding:22px 20px;border:1px solid}
.cc-healthy{border-color:rgba(34,197,94,.3);background:linear-gradient(135deg,rgba(34,197,94,.06),rgba(34,197,94,.02))}
.cc-pre{border-color:rgba(245,158,11,.3);background:linear-gradient(135deg,rgba(245,158,11,.06),rgba(245,158,11,.02))}
.cc-diab{border-color:rgba(239,68,68,.3);background:linear-gradient(135deg,rgba(239,68,68,.06),rgba(239,68,68,.02))}
.cc-icon{font-size:1.8rem;margin-bottom:8px}
.cc-label{font-family:var(--heading);font-size:1rem;font-weight:700;margin-bottom:5px}
.cc-healthy .cc-label{color:var(--green)}
.cc-pre .cc-label{color:var(--amber)}
.cc-diab .cc-label{color:var(--red)}
.cc-desc{font-size:.75rem;color:var(--muted2);line-height:1.6;margin-bottom:12px}
.cc-range{font-family:var(--mono);font-size:.6rem;padding:4px 10px;border-radius:6px;display:inline-block;letter-spacing:.04em}
.cc-healthy .cc-range{background:var(--green-dim);color:var(--green)}
.cc-pre .cc-range{background:var(--amber-dim);color:var(--amber)}
.cc-diab .cc-range{background:var(--red-dim);color:var(--red)}
.cc-count{font-family:var(--mono);font-size:.65rem;color:var(--muted);margin-top:8px}

/* ── Code block ── */
pre,code{font-family:var(--mono)}
.code-block{background:#0d1117;border:1px solid var(--border);border-radius:12px;overflow:hidden;margin-bottom:16px}
.code-header{padding:10px 16px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between}
.code-lang{font-family:var(--mono);font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--teal)}
.code-title{font-family:var(--mono);font-size:.65rem;color:var(--muted)}
.code-dots{display:flex;gap:6px}
.cdot{width:10px;height:10px;border-radius:50%}
.cd-r{background:#ff5f56}.cd-y{background:#febc2e}.cd-g{background:#27c93f}
pre{padding:20px;font-size:.78rem;line-height:1.75;overflow-x:auto;color:#c9d1d9;margin:0}
.kw{color:#ff7b72}.str{color:#a5d6ff}.cm{color:#6e7681;font-style:italic}
.fn{color:#d2a8ff}.nr{color:#79c0ff}.var{color:#ffa657}

/* ── File tree ── */
.filetree{background:#0d1117;border:1px solid var(--border);border-radius:12px;padding:20px;font-family:var(--mono);font-size:.75rem;line-height:1.9}
.ft-dir{color:var(--teal2)}.ft-py{color:var(--blue)}.ft-pkl{color:var(--purple)}
.ft-html{color:var(--amber)}.ft-csv{color:var(--green)}.ft-txt{color:var(--muted2)}
.ft-comment{color:var(--muted);font-style:italic}
.ft-indent1{padding-left:20px}.ft-indent2{padding-left:40px}

/* ── Inline badges ── */
.badge{display:inline-flex;align-items:center;gap:5px;font-family:var(--mono);font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;padding:4px 10px;border-radius:6px;border:1px solid;font-weight:500}
.b-teal{color:var(--teal);border-color:rgba(0,196,180,.3);background:var(--teal-dim)}
.b-gold{color:var(--gold2);border-color:rgba(255,200,67,.3);background:var(--gold-dim)}
.b-green{color:var(--green);border-color:rgba(34,197,94,.3);background:var(--green-dim)}
.b-red{color:var(--red);border-color:rgba(239,68,68,.3);background:var(--red-dim)}

/* ── Steps ── */
.steps{display:flex;flex-direction:column;gap:0}
.step{display:flex;gap:16px;padding:16px 0;border-bottom:1px solid rgba(30,42,66,.5)}
.step:last-child{border-bottom:none}
.step-num{width:28px;height:28px;border-radius:50%;background:var(--teal-dim);border:1px solid rgba(0,196,180,.3);color:var(--teal);font-family:var(--mono);font-size:.7rem;font-weight:600;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px}
.step-body{flex:1}
.step-title{font-family:var(--heading);font-size:.9rem;font-weight:700;color:#fff;margin-bottom:5px}
.step-desc{font-size:.8rem;color:var(--muted2);line-height:1.6}

/* ── Endpoint block ── */
.endpoint{background:var(--bg3);border:1px solid var(--border);border-radius:10px;padding:16px 18px;margin-bottom:10px;display:flex;gap:14px;align-items:flex-start}
.ep-method{font-family:var(--mono);font-size:.65rem;font-weight:600;padding:3px 10px;border-radius:5px;flex-shrink:0;letter-spacing:.06em;margin-top:2px}
.ep-get{background:var(--blue-dim);color:var(--blue);border:1px solid rgba(59,130,246,.3)}
.ep-post{background:var(--green-dim);color:var(--green);border:1px solid rgba(34,197,94,.3)}
.ep-path{font-family:var(--mono);font-size:.85rem;color:#fff;font-weight:500;margin-bottom:4px}
.ep-desc{font-size:.78rem;color:var(--muted2)}

/* ── Disclaimer ── */
.disclaimer{background:linear-gradient(135deg,rgba(239,68,68,.06),rgba(239,68,68,.02));border:1px solid rgba(239,68,68,.25);border-radius:14px;padding:20px 22px;display:flex;gap:14px;align-items:flex-start}
.disc-icon{font-size:1.3rem;flex-shrink:0;margin-top:2px}
.disc-body{flex:1}
.disc-title{font-family:var(--heading);font-size:.9rem;font-weight:700;color:var(--red);margin-bottom:6px}
.disc-text{font-size:.8rem;color:var(--muted2);line-height:1.7}

/* ── Footer ── */
footer{background:var(--bg2);border-top:1px solid var(--border);padding:28px 48px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px}
.ft-brand{font-family:var(--heading);font-size:.95rem;font-weight:700}
.ft-brand .t{color:var(--teal)}
.ft-copy{font-family:var(--mono);font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.ft-links{display:flex;gap:16px}
.ft-link{font-family:var(--mono);font-size:.6rem;letter-spacing:.08em;color:var(--muted2);text-transform:uppercase;text-decoration:none;transition:color .15s}
.ft-link:hover{color:var(--teal)}

/* ── Responsive ── */
@media(max-width:900px){
  .hero{grid-template-columns:1fr;padding:48px 24px 40px}
  .profile-card{width:100%;display:flex;align-items:center;gap:20px;text-align:left}
  .profile-ring{margin:0;flex-shrink:0}
  .p-div{display:none}
  .pipeline{grid-template-columns:repeat(3,1fr)}
  .feat-grid{grid-template-columns:1fr 1fr}
  .models-grid{grid-template-columns:1fr 1fr}
  .class-grid{grid-template-columns:1fr}
  .content{padding:0 24px 60px}
  .topbar{padding:0 24px}
  footer{padding:20px 24px}
  .hero-stats{grid-template-columns:repeat(2,1fr)}
}
@media(max-width:560px){
  .feat-grid{grid-template-columns:1fr}
  .models-grid{grid-template-columns:1fr}
  .pipeline{grid-template-columns:repeat(2,1fr)}
  .hero h1{font-size:2rem}
}
</style>
</head>
<body>

<div class="grid-bg"></div>

<!-- ── Top Bar ── -->
<nav class="topbar">
  <div class="tb-left">
    <div class="tb-logo">
      <div class="tb-logo-dot"></div>
      <div class="tb-logo-text">Vihara Tech</div>
    </div>
    <div class="tb-sep"></div>
    <div class="tb-pill">README</div>
  </div>
  <div class="tb-right">
    <div class="tb-tag">Python 3.x</div>
    <div class="tb-tag">Flask</div>
    <div class="tb-tag">Scikit-learn</div>
    <div class="tb-tag">MIT License</div>
  </div>
</nav>

<!-- ── Hero ── -->
<section class="hero">
  <div>
    <div class="hero-eyebrow"><div class="hero-eyebrow-line"></div>AI-Powered Healthcare Intelligence</div>
    <h1>Diabetes<br/><span class="hl">Prediction</span><br/>System</h1>
    <p class="hero-sub">
      A full-stack machine learning application that classifies patients as
      <strong style="color:#e2e8f0">Healthy</strong>, <strong style="color:#e2e8f0">Pre-Diabetic</strong>, or <strong style="color:#e2e8f0">Diabetic</strong>
      using an end-to-end ML pipeline — from raw clinical data through feature engineering, SMOTE balancing,
      and a tuned Decision Tree classifier served via a Flask REST API.
    </p>
    <div class="hero-chips">
      <span class="chip c-teal">&#129516; 11 Biomarkers</span>
      <span class="chip c-gold">&#128202; 3-Class Output</span>
      <span class="chip c-green">&#9889; Flask REST API</span>
      <span class="chip c-blue">&#128302; Yeo-Johnson Transform</span>
      <span class="chip c-purple">&#129516; SMOTE Balancing</span>
    </div>
    <div class="hero-stats">
      <div class="hstat"><div class="hstat-val t">15K</div><div class="hstat-lbl">Records</div></div>
      <div class="hstat"><div class="hstat-val g">23</div><div class="hstat-lbl">Raw Features</div></div>
      <div class="hstat"><div class="hstat-val gr">11</div><div class="hstat-lbl">Selected Features</div></div>
      <div class="hstat"><div class="hstat-val b">9</div><div class="hstat-lbl">ML Models Tested</div></div>
    </div>
  </div>
  <div class="profile-card">
    <div class="profile-ring">
      <div class="profile-img-inner">
        <img src="data:image/jpeg;base64,''' + photo_b64 + '''" alt="Gainaboina Madhu"/>
      </div>
    </div>
    <div>
      <div class="p-name">Gainaboina Madhu</div>
      <div class="p-role">ML Engineer</div>
      <div class="p-div"></div>
      <div class="p-skills">
        <span class="p-skill">Python</span>
        <span class="p-skill">Scikit-learn</span>
        <span class="p-skill">Flask</span>
        <span class="p-skill">XGBoost</span>
        <span class="p-skill">Pandas</span>
      </div>
    </div>
  </div>
</section>

<!-- ── Content ── -->
<div class="content">

  <!-- 01 ML Pipeline -->
  <div class="sec-head">
    <div class="sec-num">01</div>
    <div class="sec-title">ML Pipeline Architecture</div>
    <div class="sec-line"></div>
  </div>

  <div class="card">
    <div class="pipeline">
      <div class="pipe-step">
        <div class="pipe-icon pi-1">&#128196;</div>
        <div class="pipe-label">Data Ingestion</div>
        <div class="pipe-sub">15K patient records, 23 columns</div>
        <div class="pipe-arrow">&#8250;</div>
      </div>
      <div class="pipe-step">
        <div class="pipe-icon pi-2">&#128203;</div>
        <div class="pipe-label">Preprocessing</div>
        <div class="pipe-sub">Null handling, train/test split</div>
        <div class="pipe-arrow">&#8250;</div>
      </div>
      <div class="pipe-step">
        <div class="pipe-icon pi-3">&#128295;</div>
        <div class="pipe-label">Feature Eng.</div>
        <div class="pipe-sub">Yeo-Johnson, outlier capping, selection</div>
        <div class="pipe-arrow">&#8250;</div>
      </div>
      <div class="pipe-step">
        <div class="pipe-icon pi-4">&#9878;&#65039;</div>
        <div class="pipe-label">Encoding</div>
        <div class="pipe-sub">OHE for gender, Ordinal for activity/smoking</div>
        <div class="pipe-arrow">&#8250;</div>
      </div>
      <div class="pipe-step">
        <div class="pipe-icon pi-5">&#9878;&#65039;</div>
        <div class="pipe-label">SMOTE + Scaling</div>
        <div class="pipe-sub">Class balancing &amp; StandardScaler</div>
        <div class="pipe-arrow">&#8250;</div>
      </div>
      <div class="pipe-step">
        <div class="pipe-icon pi-6">&#127919;</div>
        <div class="pipe-label">Model + API</div>
        <div class="pipe-sub">Decision Tree + Flask /predict</div>
      </div>
    </div>
  </div>

  <!-- 02 Dataset -->
  <div class="sec-head">
    <div class="sec-num">02</div>
    <div class="sec-title">Dataset Overview</div>
    <div class="sec-line"></div>
  </div>

  <div class="class-grid" style="margin-bottom:16px">
    <div class="class-card cc-healthy">
      <div class="cc-icon">&#9989;</div>
      <div class="cc-label">Healthy</div>
      <div class="cc-desc">Normal glucose and metabolic markers. No diabetes risk indicators present.</div>
      <span class="cc-range">FBG &lt; 100 mg/dL &middot; HbA1c &lt; 5.7%</span>
      <div class="cc-count">4,957 records &middot; 33.1% of dataset</div>
    </div>
    <div class="class-card cc-pre">
      <div class="cc-icon">&#9888;&#65039;</div>
      <div class="cc-label">Pre-Diabetic</div>
      <div class="cc-desc">Borderline glucose levels. Lifestyle intervention can prevent progression.</div>
      <span class="cc-range">FBG 100–125 mg/dL &middot; HbA1c 5.7–6.4%</span>
      <div class="cc-count">6,264 records &middot; 41.8% of dataset</div>
    </div>
    <div class="class-card cc-diab">
      <div class="cc-icon">&#128680;</div>
      <div class="cc-label">Diabetic</div>
      <div class="cc-desc">Clinical diabetes indicators present. Immediate medical consultation required.</div>
      <span class="cc-range">FBG &ge; 126 mg/dL &middot; HbA1c &ge; 6.5%</span>
      <div class="cc-count">3,779 records &middot; 25.2% of dataset</div>
    </div>
  </div>

  <div class="card" style="padding:0;overflow:hidden">
    <table class="dtable">
      <thead>
        <tr>
          <th>Column</th><th>Type</th><th>Description</th><th>Pipeline Use</th>
        </tr>
      </thead>
      <tbody>
        <tr><td class="col-name">glucose_mg_dl</td><td><span class="col-type">float</span></td><td>Random blood glucose (mg/dL)</td><td><span class="col-use used">Selected</span></td></tr>
        <tr><td class="col-name">fasting_glucose_mg_dl</td><td><span class="col-type">float</span></td><td>Fasting plasma glucose (mg/dL)</td><td><span class="col-use used">Selected</span></td></tr>
        <tr><td class="col-name">ogtt_2hr_mg_dl</td><td><span class="col-type">float</span></td><td>2-hour OGTT glucose (mg/dL)</td><td><span class="col-use used">Selected</span></td></tr>
        <tr><td class="col-name">hba1c_pct</td><td><span class="col-type">float</span></td><td>Glycated haemoglobin (%)</td><td><span class="col-use used">Selected</span></td></tr>
        <tr><td class="col-name">age</td><td><span class="col-type">int</span></td><td>Patient age in years</td><td><span class="col-use used">Selected</span></td></tr>
        <tr><td class="col-name">sbp_mmhg</td><td><span class="col-type">int</span></td><td>Systolic blood pressure (mmHg)</td><td><span class="col-use used">Selected</span></td></tr>
        <tr><td class="col-name">bmi</td><td><span class="col-type">float</span></td><td>Body mass index (kg/m²)</td><td><span class="col-use used">Selected</span></td></tr>
        <tr><td class="col-name">family_history_diabetes</td><td><span class="col-type">int</span></td><td>Family history (0=No, 1=Yes)</td><td><span class="col-use used">Selected</span></td></tr>
        <tr><td class="col-name">gender</td><td><span class="col-type">str</span></td><td>Biological sex</td><td><span class="col-use derived">OHE → gender_Male</span></td></tr>
        <tr><td class="col-name">physical_activity</td><td><span class="col-type">str</span></td><td>Activity level (Sedentary/Light/Moderate/Active)</td><td><span class="col-use derived">Ordinal Encoded</span></td></tr>
        <tr><td class="col-name">smoking_status</td><td><span class="col-type">str</span></td><td>Smoking status (Never/Former/Current)</td><td><span class="col-use derived">Ordinal Encoded</span></td></tr>
        <tr><td class="col-name">insulin_mu_l, pregnancies</td><td><span class="col-type">float/int</span></td><td>Insulin levels, pregnancy count</td><td><span class="col-use dropped">Dropped (low corr.)</span></td></tr>
        <tr><td class="col-name">ldl, hdl, triglycerides, creatinine&hellip;</td><td><span class="col-type">float</span></td><td>Lipid panel, renal markers</td><td><span class="col-use dropped">Dropped (low corr.)</span></td></tr>
      </tbody>
    </table>
  </div>

  <!-- 03 Feature Engineering -->
  <div class="sec-head">
    <div class="sec-num">03</div>
    <div class="sec-title">Feature Engineering</div>
    <div class="sec-line"></div>
  </div>

  <div class="feat-grid">
    <div class="feat-card">
      <div class="feat-icon">&#129516;</div>
      <div class="feat-name">Yeo-Johnson Transform</div>
      <div class="feat-desc">Applied to 13 skewed numerical columns (glucose, BMI, insulin, etc.) to normalise distributions before modelling. Lambda learned on train, applied to test.</div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">&#9986;&#65039;</div>
      <div class="feat-name">Outlier Treatment</div>
      <div class="feat-desc">IQR Trimming on 12 columns; Mean±3σ Capping on 5 columns (age, SBP, creatinine, BMI, insulin). Limits computed on train set only.</div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">&#128202;</div>
      <div class="feat-name">Feature Selection</div>
      <div class="feat-desc">Variance Threshold (constant + quasi-constant removal) followed by Pearson correlation hypothesis testing (p&lt;0.05) reduced 21 features to 11 final inputs.</div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">&#128257;</div>
      <div class="feat-name">SMOTE Balancing</div>
      <div class="feat-desc">Synthetic Minority Oversampling on training set to address class imbalance across Healthy / Pre-Diabetic / Diabetic prior to model training.</div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">&#128290;</div>
      <div class="feat-name">StandardScaler</div>
      <div class="feat-desc">Z-score normalisation fitted on the SMOTE-balanced training set. Scaler persisted as <code>standard_scaler.pkl</code> and applied identically at inference time.</div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">&#128268;</div>
      <div class="feat-name">Random Imputation</div>
      <div class="feat-desc">Missing values filled by sampling from the observed distribution of each feature within the training set — preserving variance without leaking test statistics.</div>
    </div>
  </div>

  <!-- 04 Models -->
  <div class="sec-head">
    <div class="sec-num">04</div>
    <div class="sec-title">Models Evaluated</div>
    <div class="sec-line"></div>
  </div>

  <div class="models-grid">
    <div class="model-card"><div class="model-icon">&#128200;</div><div class="model-name">K-Nearest Neighbours</div><div class="model-acc ok">KNN</div><div class="model-lbl">k=5</div></div>
    <div class="model-card"><div class="model-icon">&#127891;</div><div class="model-name">Naive Bayes</div><div class="model-acc ok">GNB</div><div class="model-lbl">Gaussian</div></div>
    <div class="model-card"><div class="model-icon">&#128200;</div><div class="model-name">Logistic Regression</div><div class="model-acc ok">LR</div><div class="model-lbl">Baseline</div></div>
    <div class="model-card best"><div class="model-icon">&#127795;</div><div class="model-name">Decision Tree</div><div class="model-acc best-acc">DT ✓</div><div class="model-lbl">Final — tuned</div></div>
    <div class="model-card"><div class="model-icon">&#127795;</div><div class="model-name">Random Forest</div><div class="model-acc ok">RF</div><div class="model-lbl">n=5 trees</div></div>
    <div class="model-card"><div class="model-icon">&#9889;</div><div class="model-name">AdaBoost</div><div class="model-acc ok">ADA</div><div class="model-lbl">n=5 estimators</div></div>
    <div class="model-card"><div class="model-icon">&#128640;</div><div class="model-name">Gradient Boosting</div><div class="model-acc ok">GBM</div><div class="model-lbl">n=5 estimators</div></div>
    <div class="model-card"><div class="model-icon">&#9889;</div><div class="model-name">XGBoost</div><div class="model-acc ok">XGB</div><div class="model-lbl">n=5 estimators</div></div>
  </div>

  <div class="card">
    <p style="font-size:.82rem;color:var(--muted2);margin-bottom:12px">
      All 8 models were evaluated with micro-average ROC-AUC curves. The <strong style="color:#fff">Decision Tree</strong>
      was selected as the final model and tuned with GridSearchCV across <code style="font-family:var(--mono);font-size:.78rem;color:var(--teal)">n_estimators</code>,
      <code style="font-family:var(--mono);font-size:.78rem;color:var(--teal)">max_depth</code>,
      <code style="font-family:var(--mono);font-size:.78rem;color:var(--teal)">min_samples_split</code>, and
      <code style="font-family:var(--mono);font-size:.78rem;color:var(--teal)">min_samples_leaf</code>.
      Final hyperparameters: <strong style="color:#fff">criterion=entropy, max_depth=20, max_features=sqrt, min_samples_leaf=2, min_samples_split=5</strong>.
    </p>
    <div style="display:flex;gap:10px;flex-wrap:wrap">
      <span class="badge b-teal">criterion: entropy</span>
      <span class="badge b-gold">max_depth: 20</span>
      <span class="badge b-green">max_features: sqrt</span>
      <span class="badge b-teal">min_samples_leaf: 2</span>
      <span class="badge b-teal">min_samples_split: 5</span>
    </div>
  </div>

  <!-- 05 Project Structure -->
  <div class="sec-head">
    <div class="sec-num">05</div>
    <div class="sec-title">Project Structure</div>
    <div class="sec-line"></div>
  </div>

  <div class="filetree">
    <div><span class="ft-dir">ML_PROJECT/</span></div>
    <div class="ft-indent1"><span class="ft-dir">logs/</span> &nbsp;<span class="ft-comment"># per-module log files</span></div>
    <div class="ft-indent1"><span class="ft-dir">templates/</span></div>
    <div class="ft-indent2"><span class="ft-html">index.html</span> &nbsp;<span class="ft-comment"># Vihara Tech frontend UI</span></div>
    <div class="ft-indent1"><span class="ft-py">main.py</span> &nbsp;<span class="ft-comment"># orchestrates full pipeline</span></div>
    <div class="ft-indent1"><span class="ft-py">Variable_Transformation.py</span> &nbsp;<span class="ft-comment"># Yeo-Johnson, outliers, feature selection</span></div>
    <div class="ft-indent1"><span class="ft-py">Cat_Numerical.py</span> &nbsp;<span class="ft-comment"># OHE (gender) + Ordinal encoding</span></div>
    <div class="ft-indent1"><span class="ft-py">Balancing.py</span> &nbsp;<span class="ft-comment"># SMOTE oversampling</span></div>
    <div class="ft-indent1"><span class="ft-py">Feature_Scaling.py</span> &nbsp;<span class="ft-comment"># StandardScaler + saves Model.pkl</span></div>
    <div class="ft-indent1"><span class="ft-py">ALL_MODELS.py</span> &nbsp;<span class="ft-comment"># trains & evaluates 8 classifiers + ROC-AUC</span></div>
    <div class="ft-indent1"><span class="ft-py">hyperparameter_tuning.py</span> &nbsp;<span class="ft-comment"># GridSearchCV for Random Forest</span></div>
    <div class="ft-indent1"><span class="ft-py">logging_code.py</span> &nbsp;<span class="ft-comment"># centralised logging setup</span></div>
    <div class="ft-indent1"><span class="ft-py">app.py</span> &nbsp;<span class="ft-comment"># Flask API with startup validation</span></div>
    <div class="ft-indent1"><span class="ft-pkl">Model.pkl</span> &nbsp;<span class="ft-comment"># serialised Decision Tree classifier</span></div>
    <div class="ft-indent1"><span class="ft-pkl">standard_scaler.pkl</span> &nbsp;<span class="ft-comment"># fitted StandardScaler</span></div>
    <div class="ft-indent1"><span class="ft-csv">diabetes_dataset.csv</span> &nbsp;<span class="ft-comment"># 15,000 patient records, 23 features</span></div>
    <div class="ft-indent1"><span class="ft-txt">requirements.txt</span></div>
    <div class="ft-indent1"><span class="ft-txt">Procfile</span> &nbsp;<span class="ft-comment"># gunicorn for deployment</span></div>
  </div>

  <!-- 06 API -->
  <div class="sec-head">
    <div class="sec-num">06</div>
    <div class="sec-title">REST API Reference</div>
    <div class="sec-line"></div>
  </div>

  <div class="endpoint">
    <span class="ep-method ep-get">GET</span>
    <div><div class="ep-path">/</div><div class="ep-desc">Serves the Vihara Tech frontend diagnostic UI (templates/index.html)</div></div>
  </div>
  <div class="endpoint">
    <span class="ep-method ep-post">POST</span>
    <div>
      <div class="ep-path">/predict</div>
      <div class="ep-desc">Accepts JSON or form-data with 11 clinical features. Returns prediction label, class index, and per-class probability scores.</div>
    </div>
  </div>

  <div class="code-block">
    <div class="code-header">
      <div class="code-dots"><div class="cdot cd-r"></div><div class="cdot cd-y"></div><div class="cdot cd-g"></div></div>
      <div class="code-lang">JSON</div>
      <div class="code-title">POST /predict — request body</div>
    </div>
    <pre>{
  <span class="str">"glucose_mg_dlyeo_tri"</span>: <span class="nr">107</span>,
  <span class="str">"fasting_glucose_mg_dlyeo_tri"</span>: <span class="nr">91</span>,
  <span class="str">"ogtt_2hr_mg_dlyeo_tri"</span>: <span class="nr">119</span>,
  <span class="str">"hba1c_pctyeo_tri"</span>: <span class="nr">5.7</span>,
  <span class="str">"family_history_diabetes_tri"</span>: <span class="nr">0</span>,
  <span class="str">"age_CapMS"</span>: <span class="nr">32</span>,
  <span class="str">"sbp_mmhgyeo_CapMS"</span>: <span class="nr">102</span>,
  <span class="str">"bmi_ranyeo_CapMS"</span>: <span class="nr">27.7</span>,
  <span class="str">"gender_Male"</span>: <span class="nr">1</span>,
  <span class="str">"physical_activity_ordinal"</span>: <span class="str">"Light"</span>,
  <span class="str">"smoking_status_ordinal"</span>: <span class="str">"Never"</span>
}</pre>
  </div>

  <div class="code-block">
    <div class="code-header">
      <div class="code-dots"><div class="cdot cd-r"></div><div class="cdot cd-y"></div><div class="cdot cd-g"></div></div>
      <div class="code-lang">JSON</div>
      <div class="code-title">POST /predict — response</div>
    </div>
    <pre>{
  <span class="str">"prediction"</span>: <span class="nr">0</span>,
  <span class="str">"label"</span>: <span class="str">"Healthy"</span>,
  <span class="str">"probability"</span>: {
    <span class="str">"Healthy"</span>: <span class="nr">99.2</span>,
    <span class="str">"Pre-Diabetic"</span>: <span class="nr">0.8</span>,
    <span class="str">"Diabetic"</span>: <span class="nr">0.0</span>
  }
}</pre>
  </div>

  <!-- 07 Quick Start -->
  <div class="sec-head">
    <div class="sec-num">07</div>
    <div class="sec-title">Quick Start</div>
    <div class="sec-line"></div>
  </div>

  <div class="card">
    <div class="steps">
      <div class="step">
        <div class="step-num">1</div>
        <div class="step-body">
          <div class="step-title">Clone the repository</div>
          <div class="step-desc"><code style="font-family:var(--mono);font-size:.78rem;background:var(--bg3);padding:2px 8px;border-radius:4px;color:var(--teal)">git clone https://github.com/&lt;your-username&gt;/ai-diabetes-prediction.git &amp;&amp; cd ai-diabetes-prediction</code></div>
        </div>
      </div>
      <div class="step">
        <div class="step-num">2</div>
        <div class="step-body">
          <div class="step-title">Create virtual environment &amp; install dependencies</div>
          <div class="step-desc"><code style="font-family:var(--mono);font-size:.78rem;background:var(--bg3);padding:2px 8px;border-radius:4px;color:var(--teal)">python -m venv venv &amp;&amp; venv\Scripts\activate &amp;&amp; pip install -r requirements.txt</code></div>
        </div>
      </div>
      <div class="step">
        <div class="step-num">3</div>
        <div class="step-body">
          <div class="step-title">Run the training pipeline to generate Model.pkl and standard_scaler.pkl</div>
          <div class="step-desc"><code style="font-family:var(--mono);font-size:.78rem;background:var(--bg3);padding:2px 8px;border-radius:4px;color:var(--teal)">python main.py</code>&nbsp;&nbsp;This runs all preprocessing, balancing, scaling, and saves the model artifacts.</div>
        </div>
      </div>
      <div class="step">
        <div class="step-num">4</div>
        <div class="step-body">
          <div class="step-title">Start the Flask development server</div>
          <div class="step-desc"><code style="font-family:var(--mono);font-size:.78rem;background:var(--bg3);padding:2px 8px;border-radius:4px;color:var(--teal)">python app.py</code>&nbsp;&nbsp;Open <strong>http://localhost:5000</strong> in your browser.</div>
        </div>
      </div>
      <div class="step">
        <div class="step-num">5</div>
        <div class="step-body">
          <div class="step-title">(Optional) Production deployment with Gunicorn</div>
          <div class="step-desc"><code style="font-family:var(--mono);font-size:.78rem;background:var(--bg3);padding:2px 8px;border-radius:4px;color:var(--teal)">gunicorn app:app</code>&nbsp;&nbsp;The included <code style="font-family:var(--mono)">Procfile</code> is configured for Heroku / Render deployment.</div>
        </div>
      </div>
    </div>
  </div>

  <!-- 08 Tech Stack -->
  <div class="sec-head">
    <div class="sec-num">08</div>
    <div class="sec-title">Technology Stack</div>
    <div class="sec-line"></div>
  </div>

  <div class="feat-grid">
    <div class="feat-card">
      <div class="feat-icon">&#129520;</div>
      <div class="feat-name">Python 3.x</div>
      <div class="feat-desc">Core language. Modular pipeline split across 7 Python scripts with centralised logging via <code>logging_code.py</code>.</div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">&#129516;</div>
      <div class="feat-name">Scikit-learn</div>
      <div class="feat-desc">Decision Tree, Random Forest, KNN, Logistic Regression, SVM, StandardScaler, VarianceThreshold, GridSearchCV, and ROC-AUC evaluation.</div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">&#127760;</div>
      <div class="feat-name">Flask + Gunicorn</div>
      <div class="feat-desc">Lightweight REST API with JSON and form-data support. Startup validation detects stale model artifacts on boot. Gunicorn for production.</div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">&#128200;</div>
      <div class="feat-name">XGBoost</div>
      <div class="feat-desc">Evaluated as a candidate model alongside Gradient Boosting and AdaBoost. XGBClassifier with <code>n_estimators=5</code> used in comparative study.</div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">&#128257;</div>
      <div class="feat-name">imbalanced-learn</div>
      <div class="feat-desc">SMOTE oversampling applied to the training set to balance class distribution across Healthy, Pre-Diabetic, and Diabetic prior to fitting.</div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">&#127912;</div>
      <div class="feat-name">Custom Frontend</div>
      <div class="feat-desc">Single-page HTML/CSS/JS diagnostic UI with animated confidence bars, result popup, quick-fill test samples, and a responsive layout.</div>
    </div>
  </div>

  <!-- 09 Disclaimer -->
  <div class="sec-head">
    <div class="sec-num">09</div>
    <div class="sec-title">Medical Disclaimer</div>
    <div class="sec-line"></div>
  </div>

  <div class="disclaimer">
    <div class="disc-icon">&#9888;&#65039;</div>
    <div class="disc-body">
      <div class="disc-title">Research &amp; Educational Use Only</div>
      <div class="disc-text">
        This system is developed strictly for <strong>academic research and educational demonstration purposes</strong>.
        It is <strong>not</strong> a certified medical device and does <strong>not</strong> constitute a clinical diagnosis.
        Predictions made by this model must never be used as a substitute for professional medical advice, examination,
        or diagnosis by a qualified healthcare provider. Always consult a licensed physician or endocrinologist
        for any diabetes-related health concerns.
      </div>
    </div>
  </div>

</div>

<!-- ── Footer ── -->
<footer>
  <div class="ft-brand"><span class="t">Vihara Tech</span> &mdash; AI Diabetes Prediction System</div>
  <div class="ft-links">
    <a class="ft-link" href="#">Documentation</a>
    <a class="ft-link" href="#">Issues</a>
    <a class="ft-link" href="#">License</a>
  </div>
  <div class="ft-copy">Built by Gainaboina Madhu &middot; Research Use Only</div>
</footer>

</body>
</html>'''

with open('/mnt/user-data/outputs/README.html', 'w') as f:
    f.write(readme)
print("Done, size:", len(readme))
PYEOF
Output

Done, size: 389206
Done
