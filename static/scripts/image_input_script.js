const file = document.querySelector('#id_cover_image') || document.querySelector('#id_avatar_image');
file.addEventListener('change', (e) => {
    // Get the selected file
    const [file] = e.target.files;
    // Get the file name and size
    const {name: fileName, size} = file;
    // Convert size in bytes to kilo bytes
    const fileSize = (size / 1000).toFixed(2);
    // Set the text content
    document.querySelector('.file-name').textContent = `${fileName} - ${fileSize}KB`;
});
