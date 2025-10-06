const $ = (sel) => document.querySelector(sel);

// Display elements
const hEl = $("#hours");
const mEl = $("#minutes");
const sEl = $("#seconds");
const msEl = $("#ms");

// Buttons
const startBtn = $("#startBtn");
const stopBtn  = $("#stopBtn");
const resetBtn = $("#resetBtn");
const lapBtn   = $("#lapBtn");
const themeBtn = $("#themeBtn");

// Laps list
const lapsEl = $("#laps");

// State
let intervalId = null;
let startTimestamp = 0;      // when current run started (ms since epoch)
let accumulated = 0;         // total elapsed across all runs (ms)
let running = false;

// Utilities
const pad2 = (n) => String(n).padStart(2, "0");
const pad3 = (n) => String(n).padStart(3, "0");

// function pad1 (n){
//   return String(n).padStart(2, "0");
// }

// Render HH:MM:SS.mmm
function render(ms){
  const hours = Math.floor(ms / 3_600_000);
  const minutes = Math.floor((ms % 3_600_000) / 60_000);
  const seconds = Math.floor((ms % 60_000) / 1000);
  const millis  = ms % 1000;

 hEl.textContent  = pad2(hours);
  mEl.textContent  = pad2(minutes);
  sEl.textContent  = pad2(seconds);
  msEl.textContent = "." + pad3(millis);
}

// Start
function start(){
  if (running) return; // prevent multiple timers
  running = true;
  startTimestamp = Date.now();
  intervalId = setInterval(tick, 10); // 10ms for milliseconds display
  startBtn.disabled = true;
  stopBtn.disabled  = false;
  resetBtn.disabled = false;
  lapBtn.disabled   = false;
}

// Stop (pause)                                
function stop(){
  if (!running) return;
  running = false;
  clearInterval(intervalId);
  intervalId = null;
  accumulated += Date.now() - startTimestamp;
  startBtn.disabled = false;
  stopBtn.disabled  = true;
}

// Reset
function reset(){
  clearInterval(intervalId);
  intervalId = null;
  running = false;
  accumulated = 0;
  render(0);
  lapsEl.innerHTML = "";
  startBtn.disabled = false;
  stopBtn.disabled  = true;
  resetBtn.disabled = true;
  lapBtn.disabled   = true;
}

// Tick (every 10ms)
function tick(){
  const now = Date.now();
  const elapsed = accumulated + (now - startTimestamp);
  render(elapsed);
}

// Lap 
function lap(){
  const displayTime = `${hEl.textContent}:${mEl.textContent}:${sEl.textContent}${msEl.textContent}`;
  const li = document.createElement("li");
  const index = lapsEl.children.length + 1;
  li.innerHTML = `<span class="label">Lap ${pad2(index)}</span><span class="time">${displayTime}</span>`;
  lapsEl.prepend(li);
}

// Theme toggle
function toggleTheme(){
  const app = document.querySelector(".app");
  const isLight = app.getAttribute("data-theme") === "light";
  app.setAttribute("data-theme", isLight ? "dark" : "light");
  themeBtn.setAttribute("aria-pressed", String(!isLight));
}

// Keyboard shortcuts 
document.addEventListener("keydown", (e) => {
  if (e.code === "Space"){ e.preventDefault(); running ? stop() : start(); }
  if (e.key.toLowerCase() === "r") reset();
  if (e.key.toLowerCase() === "l") { if (!lapBtn.disabled) lap(); }
  if (e.key.toLowerCase() === "t") toggleTheme();
});

// Wire up listeners
startBtn.addEventListener("click", start);
stopBtn .addEventListener("click", stop);
resetBtn.addEventListener("click", reset);
lapBtn  .addEventListener("click", lap);
themeBtn.addEventListener("click", toggleTheme);

// Initial render
render(0); 
