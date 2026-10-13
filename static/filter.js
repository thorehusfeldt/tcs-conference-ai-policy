// Filter the table by venue, keeping the choice in the URL, and unfold a conference
// into its years, and a year into the versions of its call for papers.
// An unfolded row is replaced by what it unfolds into.
const form = document.getElementById("filters");
const boxes = [...form.querySelectorAll("input[type=checkbox]")];
const rows = [...document.querySelectorAll("#policies tbody tr")];
const open = new Set();

function apply() {
  const venues = boxes.filter((b) => b.checked).map((b) => b.value);
  for (const row of rows) {
    const { level, series, round, venue } = row.dataset;
    const visible = {
      series: !open.has(series),
      header: open.has(series),
      round: open.has(series) && !open.has(round),
      version: open.has(series) && open.has(round),
    }[level];
    row.hidden = !(venues.includes(venue) && visible);
  }
  const query = boxes.every((b) => b.checked) ? "" : `?venue=${venues.join(",")}`;
  history.replaceState(null, "", query || location.pathname);
}

const wanted = new URLSearchParams(location.search).get("venue");
for (const box of boxes) {
  if (wanted !== null) box.checked = wanted.split(",").includes(box.value);
  box.addEventListener("change", apply);
}
for (const button of document.querySelectorAll("#policies .toggle")) {
  button.addEventListener("click", () => {
    const key = button.dataset.series ?? button.dataset.round;
    if (!open.delete(key)) open.add(key);
    apply();
  });
}
form.hidden = false;
apply();
