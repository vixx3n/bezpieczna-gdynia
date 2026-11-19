const status = document.getElementById("data-status");

async function loadData() {
  try {
    const response = await fetch("./data/accidents.json");
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const records = await response.json();
    const totals = { accidents: 0, injured: 0, deaths: 0 };

    for (const record of records) {
      totals.accidents += record.accidents;
      totals.injured += record.injured;
      totals.deaths += record.deaths;
    }

    document.getElementById("accidents").textContent = totals.accidents;
    document.getElementById("injured").textContent = totals.injured;
    document.getElementById("deaths").textContent = totals.deaths;

    const first = records[0].quarter;
    const last = records[records.length - 1].quarter;
    status.textContent = `Sumy za okres od ${first} do ${last}.`;
  } catch (error) {
    status.textContent = "Nie udało się wczytać danych.";
    console.error(error);
  }
}

loadData();