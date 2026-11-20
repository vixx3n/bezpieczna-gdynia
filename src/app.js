const yearFilter = document.getElementById("year-filter");
const statusElement = document.getElementById("data-status");

function showAccidentChart(records) {
  const chart = document.getElementById("accident-chart");
  const note = document.getElementById("chart-note");
  const quarters = records.slice(-4);

  chart.replaceChildren();
  note.textContent = yearFilter.value === "all"
    ? "Widzisz ostatnie 4 dostępne kwartały. Wybierz rok, żeby zobaczyć wcześniejsze."
    : "Widzisz dostępne kwartały wybranego roku.";

  const max = Math.max(1, ...quarters.map(record => record.accidents));

  for (const record of quarters) {
    const item = document.createElement("li");
    item.textContent = `${record.quarter}: ${record.accidents} wypadków `;

    const bar = document.createElement("meter");
    bar.min = 0;
    bar.max = max;
    bar.value = record.accidents;
    bar.setAttribute("aria-label", `Liczba wypadków w ${record.quarter}`);

    item.appendChild(bar);
    chart.appendChild(item);
  }
}

function showStats(records) {
  const year = yearFilter.value;
  const selectedRecords = year === "all"
    ? records
    : records.filter(record => record.quarter.slice(0, 4) === year);

  const totals = { accidents: 0, injured: 0, deaths: 0 };

  for (const record of selectedRecords) {
    totals.accidents += record.accidents;
    totals.injured += record.injured;
    totals.deaths += record.deaths;
  }

  document.getElementById("accidents").textContent = totals.accidents;
  document.getElementById("injured").textContent = totals.injured;
  document.getElementById("deaths").textContent = totals.deaths;

  showAccidentChart(selectedRecords);

  const first = selectedRecords[0].quarter;
  const last = selectedRecords[selectedRecords.length - 1].quarter;
  statusElement.textContent = first === last
    ? `Wyniki za ${first}.`
    : `Sumy za okres od ${first} do ${last}.`;

  if (year !== "all" && selectedRecords.length < 4) {
    statusElement.textContent += " Dane za ten rok są niepełne.";
  }
}

async function loadData() {
  try {
    const response = await fetch("./data/accidents.json");
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const records = await response.json();
    const years = [...new Set(records.map(record => record.quarter.slice(0, 4)))];

    for (const year of years.sort().reverse()) {
      const option = document.createElement("option");
      option.value = year;
      option.textContent = year;
      yearFilter.appendChild(option);
    }

    yearFilter.addEventListener("change", () => showStats(records));
    showStats(records);
    yearFilter.disabled = false;
  } catch (error) {
    statusElement.textContent = "Nie udało się wczytać danych.";
    console.error(error);
  }
}

loadData();