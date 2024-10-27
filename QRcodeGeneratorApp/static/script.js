const saveBackgroundInactive = '#ccc';

// Constant that store the default colors for logos
const defaultColors = {
    facebook: {
        cc: '#000000', // Center Color
        ec: '#0000ff', // Edge Color
        bc: '#ffffff'   // Back Color
    },
    instagram: {
        cc: '#f9ce34', // Center Color
        ec: '#840cf6', // Edge Color
        bc: '#ffffff'   // Back Color
    },
    default: {
        cc: '#000000', // Reset to default (black)
        ec: '#000000', // Reset to default (black)
        bc: '#ffffff'  // Default back color
    }
};

// Constant that store used DOM elements
const elements = {
    saveButton: document.getElementById('saveQRCodeButton'),
    logo: document.getElementById('logo'),
    style: document.getElementById('style'),
    size: document.getElementById('size'),
    link: document.getElementById('link'),
    color: document.getElementById('color'),
    ccColor: document.getElementById('ccColor'),
    ecColor: document.getElementById('ecColor'),
    bcColor: document.getElementById('bcColor'),
    ccLabel: document.getElementById('ccLabel'),
    ecLabel: document.getElementById('ecLabel'),
    fileUploadRow: document.getElementById('fileUploadRow'),
    fillDropdown: document.getElementById('color-fill'),
    fillBox: document.getElementById('color-fill-box'),
    qrCodeImage: document.getElementById('qrCodeImage'),
};


// Function to toggle save button and form inputs
function toggleSaveButton(isEnabled) {
    elements.saveButton.disabled = !isEnabled;
    elements.saveButton.style.backgroundColor = isEnabled ? '' : saveBackgroundInactive;
    elements.saveButton.style.cursor = isEnabled ? 'pointer' : 'not-allowed';

    ['logo', 'style', 'size', 'link', 'color', 'ccColor', 'ecColor', 'bcColor'].forEach(id => {
        elements[id].disabled = !isEnabled;
    });
}

// Enable or disable color inputs based on selection
function toggleColorInputs(enable) {
    ['ccColor', 'ecColor', 'bcColor'].forEach(id => {
        elements[id].disabled = !enable;
        elements[id].style.pointerEvents = enable ? 'auto' : 'none';  // Disable interaction for color picker
        elements[id].style.cursor = enable ? 'pointer' : 'not-allowed';  // Change cursor to disabled style
    });
}

// Function to disable the save button while generating the QR code
function initialDisableSaveButton() {
    const saveButton = document.getElementById('saveQRCodeButton'); //Save Button element
    saveButton.disabled = true; // Disable the save button element
    saveButton.style.backgroundColor = saveBackgroundInactive; // Change the background color to gray
    saveButton.style.cursor = 'not-allowed'; // Change cursor to indicate it's disabled
}
// Function to update color inputs based on selected logo
function updateColorInputs(logo) {
    let colors = defaultColors[logo] || defaultColors.default; // Set default colors based on selected logo and chosen color
    if (elements.color.value === 'none') {
        colors = defaultColors.default
    }
    elements.ccColor.value = colors.cc; // Update center color value
    elements.ecColor.value = colors.ec; // Update edge color value
    elements.bcColor.value = colors.bc; // Update back color value
    toggleColorInputs(elements.color.value === 'custom'); //Enable or disable color inputs based on color choice

}

// Function to validate hex color format
function validateHex(hex) {
    return /^#[0-9A-Fa-f]{6}$/.test(hex);
}


// Function to display the QR code image
function displayQRCode(item) {
    elements.qrCodeImage.src = `data:image/png;base64,${item.qr_code_image}`; // Format base64 image
    elements.qrCodeImage.style.display = 'block'; // Show the image
    elements.qrCodeImage.onload = () => {
        toggleSaveButton(true); // Enable the save button
    };
}

// Function to save qr code image locally
function save() {
    const link = document.createElement('a');
    link.href = document.getElementById('qrCodeImage').src;
    link.download = 'qrcode.png';
    link.click();
    link.delete;
    clear()
}

// Function that display colors upon fill value selection
function colorFill(fillValue) {
    if (fillValue === 'solid') {
        elements.ccLabel.value = 'front'; // Change label value of element
        elements.ecColor.style.display = 'none'; // Hide element
        elements.ecLabel.style.display = 'none'; // Hide label of element
    } else {
        elements.ccLabel.value = 'center'; // Change name of element
        elements.ecColor.style.display = 'flex'; // Display element
        elements.ecLabel.style.display = 'flex'; // Display label of element
    }
}

function clear() {
    elements.logo.value = "";
    elements.style.value = "default";
    elements.size.value = "default";
    elements.link.value = '';
    elements.color.value = "default";
    elements.ccColor.value = defaultColors.default.cc
    elements.ccColor.style.display = 'flex';
    elements.ecColor.value = defaultColors.default.ec
    elements.ecColor.style.display = 'flex';
    elements.bcColor.value = defaultColors.default.bc
    elements.ccLabel.value = 'center'
    elements.ccLabel.style.display = 'flex';
    elements.ecLabel.value = 'edge'
    elements.ecLabel.style.display = 'flex';
    elements.fileUploadRow.style.display ="none";
    elements.fillDropdown.value = "gradient"
    elements.fillBox.style.display ="none";
    elements.qrCodeImage.src = "../static/logos/pomarina.png"
}


initialDisableSaveButton() // Run when scrypt is activated

// Event listener for logo selection
document.getElementById('logo').addEventListener('change', function () {
    const logo = this.value; // Chosen Logo value
    const fileUploadRow = document.getElementById('fileUploadRow'); // File upload element
    const defaultOption = document.querySelector("#color option[value='default']"); // Default color option
    const colorDropdown = document.getElementById('color'); // Color options element
    const fillDropdown = document.getElementById('color-fill'); // Color options element

    // Toggle file input visibility for custom logo
    fileUploadRow.style.display = (logo === 'custom') ? 'flex' : 'none';

    // Show/hide default color option
    if (logo === 'none' || logo === 'custom') {
        if (defaultOption) {
            defaultOption.style.display = 'none'; // Clear default option
            colorDropdown.selectedIndex = 0; // Set to a different option (0 = "No Color")
            displayFill() // Display or hide color elements upon color value selection
        }
    } else {

        if (defaultOption) {
            defaultOption.style.display = 'block'; // Set default option
            colorDropdown.selectedIndex = 2; // Show the default option
            fillDropdown.selectedIndex = 1; // Select gradient option if fb or ig
            displayFill() // Display or hide color elements upon color value selection
        }
    }
    updateColorInputs(logo) // Update color inputs based on selected logo

});


// Listen for the form change event
document.getElementById('userForm').addEventListener('change', async function (event) {
    event.preventDefault();
    const formData = new FormData(); //Create empty form data
    toggleSaveButton(false); // Disable Save button

    // Validate color inputs
    if (!validateHex(elements.ccColor.value) || !validateHex(elements.ecColor.value) || !validateHex(elements.bcColor.value)) {
        alert("Please enter valid hex color codes (e.g., #rrggbb).");
        return;
    }

    // Add form fields to FormData object
    formData.append('logo', elements.logo.value); // Add logo data to form
    formData.append('link', elements.link.value); // Add link data to form
    formData.append('cc', elements.ccColor.value); // Add center color data to form
    formData.append('ec', elements.fillDropdown.value === 'solid' && elements.color.value === 'custom' ?
        elements.ccColor.value : elements.ecColor.value); // Add edge color data to form
    formData.append('bc', elements.bcColor.value); // Add back color data to form
    formData.append('style', elements.style.value); // Add style data to form
    formData.append('size', elements.size.value); // Add size data to form

    // If a custom logo is selected, append the file path to FormData
    if (elements.logo.value === 'custom') {
        const logoFile = document.getElementById('logoFile').files[0];
        if (logoFile) formData.append('logoFile', logoFile); // Append the logo file path
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/',
            {
                method: 'POST',
                body: formData // No need to set Content-Type, let the browser do it
                }
            );
        if (response.ok) {
            const result = await response.json();
            displayQRCode(result); // Display QR code
            let currentColor = document.getElementById('color').value
            // console.log(currentColor == 'custom');
            toggleColorInputs(currentColor === 'custom');
            // displayFill()
        } else {
            const errorMessage = await response.text();
            console.error('Error:', response.statusText, errorMessage);
            alert(`Error: ${response.statusText}`);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while generating the QR code. Please try again.');
    }
});

// Listen for the color fill changes
document.getElementById('color-fill').addEventListener('change', function () {
    const fillValue = this.value; // Fill color value
    colorFill(fillValue) // Display colors upon fill value selection
    displayFill() // Display or hide color elements upon color value selection
});

// Add an event listener to the color selection dropdown
document.getElementById('color').addEventListener('change', function () {
    updateColorInputs(elements.logo.value) // Update color inputs based on selected logo
    displayFill() // Display or hide color elements upon color value selection
});

// Function that display or hide color elements upon color value selection
function displayFill() {
    const isCustom = elements.color.value === 'custom'; // Check if color value is custom or not

    elements.fillBox.style.display = isCustom ? 'flex' : 'none'; // Display or Hide element
    if (elements.color.value === 'none') {
        elements.ecColor.style.display = 'none'; // Hide Edge Color element
        elements.ccLabel.value = 'front'; // Change name of central element
        elements.ecLabel.style.display = 'none'; // Hide edge label
        elements.ecColor.style.display = 'none'; // Hide edge element
    } else {
        elements.ecColor.style.display = 'flex'; // Display Edge Color element
        colorFill(elements.fillDropdown.value); // Display colors upon fill value selection
    }
    toggleColorInputs(isCustom);
}


