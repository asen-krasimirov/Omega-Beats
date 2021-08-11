const copyTextElem = document.querySelector(".feed-back-btn");
const inputElem = document.querySelector('#url-holder')

if (copyTextElem) copyTextElem.addEventListener('click', copyText)


function copyText() {

    /* Select the text field */
    inputElem.style.display = 'inline';
    inputElem.textContent = window.location.href;
    inputElem.focus();
    inputElem.select();
    inputElem.setSelectionRange(0, 99999)

    document.execCommand("copy");

    inputElem.style.display = 'none';

    /* Change button text*/
    copyTextElem.textContent = 'Link Copied';
}
