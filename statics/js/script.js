const translateButton = document.getElementById('translate-button');
const inputWord = document.getElementById('input-word');
const outputWord = document.getElementById('output-word');

translateButton.addEventListener('click', () => {
  const input = inputWord.value;
  // Tarjima logikasini shu joyda yozasiz
  const output = translate(input);
  outputWord.textContent = output;
});

function translate(input) {
  // Tarjima logikasini shu funksiya orqali yozasiz
  // Misol uchun:
  if (input === 'apple') {
    return 'olma';
  } else if (input === 'cat') {
    return 'mushuk';
  } else {
    return 'Tarjima topilmadi';
  }
}