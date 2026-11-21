"use strict";

async function RunSentimentAnalysis() {
  const text = document.getElementById("textToAnalyze").value;
  const output = document.getElementById("systemResponse");
  const button = document.getElementById("analyzeButton");
  output.textContent = "Analyzing...";
  button.disabled = true;
  try {
    const response = await fetch(
      "/emotionDetector?textToAnalyze=" + encodeURIComponent(text)
    );
    const result = await response.text();
    output.textContent = result;
    output.classList.toggle("error", !response.ok);
  } catch (error) {
    output.textContent = "Unable to reach the application. Please try again.";
    output.classList.add("error");
  } finally {
    button.disabled = false;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("analyzeButton")
    .addEventListener("click", RunSentimentAnalysis);
});
