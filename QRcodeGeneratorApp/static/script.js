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

// Function to enable color input fields
function enableColorInputs() {
    document.getElementById('ccColor').disabled = false; // Enable Center Color element
    document.getElementById('ecColor').disabled = false; // Enable Edge Color element
    document.getElementById('bcColor').disabled = false; // Enable Back Color element
}

// Function to disable color input fields
function disableColorInputs() {
    document.getElementById('ccColor').disabled = true; // Disable Center Color element
    document.getElementById('ecColor').disabled = true; // Disable Edge Color element
    document.getElementById('bcColor').disabled = true; // Disable Back Color element
}

// Function to disable the save button while generating the QR code
function disableSaveButton() {
    const saveButton = document.getElementById('saveQRCodeButton'); //Save Button element
    const logo = document.getElementById('logo'); // Chosen Logo element
    const style = document.getElementById('style'); // Chosen Style element
    const size = document.getElementById('size'); // Chosen Size element
    const link = document.getElementById('link'); // Input link data element
    const color = document.getElementById('color'); // Chosen Color element
    const ccColor = document.getElementById('ccColor'); // Center Color element
    const ecColor = document.getElementById('ecColor'); // Edge Color element
    const bcColor = document.getElementById('bcColor'); // Back Color element
    saveButton.disabled = true; // Disable the save button
    saveButton.style.backgroundColor = '#ccc'; // Change the background color to gray
    saveButton.style.cursor = 'not-allowed'; // Change cursor to indicate it's disabled
    logo.disabled = true; // Disable Logo element
    style.disabled = true; // Disable Style element
    size.disabled = true; // Disable Size element
    link.disabled = true; // Disable Link element
    color.disabled = true; // Disable Color element
    ccColor.disabled = true; // Disable Center Color element
    ecColor.disabled = true; // Disable Edge Color element
    bcColor.disabled = true; // Disable Back Color element
}

// Function to disable the save button while generating the QR code
function initialDisableSaveButton() {
    const saveButton = document.getElementById('saveQRCodeButton'); //Save Button element
    saveButton.disabled = true; // Disable the save button element
    saveButton.style.backgroundColor = '#ccc'; // Change the background color to gray
    saveButton.style.cursor = 'not-allowed'; // Change cursor to indicate it's disabled
}

// Function to enable the save button after QR code is generated
function enableSaveButton() {
    const saveButton = document.getElementById('saveQRCodeButton'); //Save Button element
    const logo = document.getElementById('logo'); // Chosen Logo element
    const style = document.getElementById('style'); // Chosen Style element
    const size = document.getElementById('size'); // Chosen Size element
    const link = document.getElementById('link'); // Input link data element
    const color = document.getElementById('color'); // Chosen Color element
    const ccColor = document.getElementById('ccColor'); // Center Color element
    const ecColor = document.getElementById('ecColor'); // Edge Color element
    const bcColor = document.getElementById('bcColor'); // Back Color element
    saveButton.disabled = false; // Enable the save button element
    saveButton.style.backgroundColor = ''; // Restore default background color
    saveButton.style.cursor = ''; // Restore default cursor
    logo.disabled = false; // Enable Logo element
    style.disabled = false; // Enable Style element
    size.disabled = false; // Enable Size element
    link.disabled = false; // Enable Link element
    color.disabled = false; // Enable Color element
    ccColor.disabled = false; // Enable Center Color element
    ecColor.disabled = false; // Enable Edge Color element
    bcColor.disabled = false; // Enable Back Color element
}
// Function to enable or disable color inputs based on color choice
function checkColorInputs() {
    const colorChoice = document.getElementById('color').value; // Chosen Color
    if (colorChoice === 'custom') {
        enableColorInputs(); // Enable color inputs for custom colors
    } else {
        disableColorInputs(); // Disable color inputs for non-custom colors
    }
}

// Function to update color inputs based on selected logo
function updateColorInputs(logo) {
    const ccColorInput = document.getElementById('ccColor'); // Center Color element
    const ecColorInput = document.getElementById('ecColor'); // Edge Color element
    const bcColorInput = document.getElementById('bcColor'); // Back Color element
    const colorChoice = document.getElementById('color').value; // Chosen Color

    let colors = defaultColors.default; // Default colors

    // Set default colors based on selected logo and chosen color
    if (logo in defaultColors) {
        colors = defaultColors[logo]; // Get colors for the selected logo
        }
    if (colorChoice === 'none') {
        colors = defaultColors.default; // Default colors
    }

    ccColorInput.value = colors.cc; // Update center color value
    ecColorInput.value = colors.ec; // Update edge color value
    bcColorInput.value = colors.bc; // Update back color value
    checkColorInputs(); //Enable or disable color inputs based on color choice
}

// Function to validate hex color format
function validateHex(hex) {
    const hexColorPattern = /^#[0-9A-Fa-f]{6}$/; // Matches format #rrggbb
    return hexColorPattern.test(hex);
}

// Function to display the QR code image
function displayQRCode(item) {
    const qrCodeImage = document.getElementById('qrCodeImage'); //QR code image element
    qrCodeImage.src = `data:image/png;base64,${item.qr_code_image}`; // Format base64 image
    qrCodeImage.style.display = 'block'; // Show the image
    enableSaveButton(); // Enable save button element after QR code is generated

    // Show the save button
    const saveButton = document.getElementById('saveQRCodeButton'); //Save Button element
    saveButton.style.display = 'block'; // Make the save button visible

    // Set up download functionality
    saveButton.onclick = function () {
        const link = document.createElement('a'); // Create an anchor element
        link.href = qrCodeImage.src; // Set the href to the QR code image source
        link.download = 'qrcode.png'; // Specify the default filename
        link.click(); // Programmatically click the link to trigger the download
    };
}

//
function colorFill(fillValue) {
    const edgeElement = document.getElementById('ecColor');
    const centerLabel = document.getElementById('ccLabel');
    const edgeLabel = document.getElementById('ecLabel');
    if (fillValue === 'solid') {
        centerLabel.value = 'front';
        edgeElement.style.display = 'none';
        edgeLabel.style.display = 'none';
    } else {
        centerLabel.value = 'center';
        edgeElement.style.display = 'flex';
        edgeLabel.style.display = 'flex';
    }
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
            displayFill()
        }
    } else {

        if (defaultOption) {
            defaultOption.style.display = 'block'; // Set default option
            colorDropdown.selectedIndex = 2; // Show the default option
            fillDropdown.selectedIndex = 1; // Select gradient option if fb or ig
            displayFill()
        }
    }
    updateColorInputs(logo) // Update color inputs based on selected logo

});

function displayFill() {
    const color = document.getElementById('color').value; // Selected color value
    const fill = document.getElementById('color-fill-box')
    const fillValue = document.getElementById('color-fill').value
    if (color === 'custom') {
        fill.style.display = 'flex'
        colorFill(fillValue)
    }
    else if (color === 'none') {
        fill.style.display = 'none'
        const edgeElement = document.getElementById('ecColor');
        const centerLabel = document.getElementById('ccLabel');
        const edgeLabel = document.getElementById('ecLabel');
        centerLabel.value = 'front';
        edgeElement.style.display = 'none';
        edgeLabel.style.display = 'none';
    }
    else {
        fill.style.display = 'none'
        colorFill(fillValue)
    }
    // console.log(fillValue)
}

// Add an event listener to the color selection dropdown
document.getElementById('color').addEventListener('change', function () {
    const logo = document.getElementById('logo').value; // Selected logo
    updateColorInputs(logo) // Update color inputs based on selected logo
    displayFill()
});

// Listen for the form submission event
document.getElementById('userForm').addEventListener('change', async function (event) {
    event.preventDefault();
    let formData = new FormData(); //Create empty form data
    disableSaveButton(); // Disable the save button while generating the QR code
    // displayFill()
    // Collect form data
    const logo = document.getElementById('logo').value; // Chosen logo value
    const link = document.getElementById('link').value; // Chosen link value
    const cc = document.getElementById('ccColor').value; // Chosen center color value
    const ec = document.getElementById('ecColor').value; // Chosen edge color value
    const bc = document.getElementById('bcColor').value; // Chosen back color value
    const style = document.getElementById('style').value; // Chosen style value
    const size = document.getElementById('size').value; // Chosen size value
    const fill = document.getElementById('color-fill').value; // Chosen fill value
    const color = document.getElementById('color').value; // Chosen fill value

    // Validate color inputs
    if (!validateHex(cc) || !validateHex(ec) || !validateHex(bc)) {
        alert("Please enter valid hex color codes (e.g., #rrggbb).");
        return;
    }

    // Add form fields to FormData object
    formData.append('logo', logo); // Add logo data to form
    formData.append('link', link); // Add link data to form
    formData.append('cc', cc); // Add center color data to form
    if (fill === 'solid' && color === 'custom') {
        formData.append('ec', cc); // Add edge color data to form
    } else {
        formData.append('ec', ec); // Add edge color data to form
    }
    formData.append('bc', bc); // Add back color data to form
    formData.append('style', style); // Add style data to form
    formData.append('size', size); // Add size data to form

    // If a custom logo is selected, append the file path to FormData
    if (logo === 'custom') {
        const logoFile = document.getElementById('logoFile').files[0];
        if (logoFile) {
            formData.append('logoFile', logoFile); // Append the logo file path
        }
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
            checkColorInputs()
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

document.getElementById('color-fill').addEventListener('change', function () {
    const fillValue = this.value; // Fill color value
    displayFill()
    colorFill(fillValue)
});