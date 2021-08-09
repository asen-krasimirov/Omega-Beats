const keyTexts = [...document.querySelectorAll('.key-text')]

if (keyTexts) document.querySelector('.map-button').addEventListener('click', () => {
    for (const key of keyTexts) {
        key.classList.toggle('show');
    }
});
