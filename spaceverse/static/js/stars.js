(() => {
  const canvas = document.getElementById("starfield");
  if (!canvas) return;

  const ctx = canvas.getContext("2d");
  let w, h, dpr;

  function resize(){
    dpr = window.devicePixelRatio || 1;
    w = canvas.clientWidth = window.innerWidth;
    h = canvas.clientHeight = window.innerHeight;
    canvas.width = Math.floor(w * dpr);
    canvas.height = Math.floor(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  window.addEventListener("resize", resize);
  resize();

  const stars = [];
  const STAR_COUNT = Math.min(220, Math.floor((w*h)/7000));

  function rand(min, max){ return Math.random() * (max - min) + min; }

  for (let i=0; i<STAR_COUNT; i++){
    stars.push({
      x: rand(0, w),
      y: rand(0, h),
      r: rand(0.6, 1.8),
      a: rand(0.25, 0.95),
      vx: rand(-0.08, 0.12),
      vy: rand(0.02, 0.22),
      tw: rand(0.002, 0.01)
    });
  }

  function tick(){
    ctx.clearRect(0,0,w,h);

    // soft nebula haze
    const g = ctx.createRadialGradient(w*0.2, h*0.1, 20, w*0.2, h*0.1, Math.max(w,h)*0.9);
    g.addColorStop(0, "rgba(124,92,255,0.10)");
    g.addColorStop(1, "rgba(0,0,0,0)");
    ctx.fillStyle = g;
    ctx.fillRect(0,0,w,h);

    for (const s of stars){
      s.x += s.vx;
      s.y += s.vy;
      s.a += Math.sin(performance.now()*s.tw) * 0.003;

      if (s.x < -10) s.x = w+10;
      if (s.x > w+10) s.x = -10;
      if (s.y > h+10) s.y = -10;

      ctx.beginPath();
      ctx.fillStyle = `rgba(234,240,255,${Math.max(0.15, Math.min(1, s.a))})`;
      ctx.arc(s.x, s.y, s.r, 0, Math.PI*2);
      ctx.fill();
    }

    requestAnimationFrame(tick);
  }
  tick();
})();