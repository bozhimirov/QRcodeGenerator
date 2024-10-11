// Store the default colors for logos
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
    document.getElementById('ccColor').disabled = false; // Enable Center Color
    document.getElementById('ecColor').disabled = false; // Enable Edge Color
    document.getElementById('bcColor').disabled = false; // Enable Back Color
}

// Function to disable color input fields
function disableColorInputs() {
    document.getElementById('ccColor').disabled = true; // Disable Center Color
    document.getElementById('ecColor').disabled = true; // Disable Edge Color
    document.getElementById('bcColor').disabled = true; // Disable Back Color
}

// Function to disable the save button while generating the QR code
function disableSaveButton() {
    const saveButton = document.getElementById('saveQRCodeButton');
    const logo = document.getElementById('logo');
    const style = document.getElementById('style');
    const size = document.getElementById('size');
    const link = document.getElementById('link');
    const color = document.getElementById('color');
    const ccColor = document.getElementById('ccColor');
    const ecColor = document.getElementById('ecColor');
    const bcColor = document.getElementById('bcColor');
    saveButton.disabled = true; // Disable the save button
    saveButton.style.backgroundColor = '#ccc'; // Change the background color to gray
    saveButton.style.cursor = 'not-allowed'; // Change cursor to indicate it's disabled
    logo.disabled = true
    style.disabled = true
    size.disabled = true
    link.disabled = true
    color.disabled = true
    ccColor.disabled = true
    ecColor.disabled = true
    bcColor.disabled = true
}
// Function to disable the save button while generating the QR code
function initialdisableSaveButton() {
    const saveButton = document.getElementById('saveQRCodeButton');

    saveButton.disabled = true; // Disable the save button
    saveButton.style.backgroundColor = '#ccc'; // Change the background color to gray
    saveButton.style.cursor = 'not-allowed'; // Change cursor to indicate it's disabled

}
initialdisableSaveButton()
// Function to enable the save button after QR code is generated
function enableSaveButton() {
    const saveButton = document.getElementById('saveQRCodeButton');
    const logo = document.getElementById('logo');
    const style = document.getElementById('style');
    const size = document.getElementById('size');
    const link = document.getElementById('link');
    const color = document.getElementById('color');
    const ccColor = document.getElementById('ccColor');
    const ecColor = document.getElementById('ecColor');
    const bcColor = document.getElementById('bcColor');
    saveButton.disabled = false; // Enable the save button
    saveButton.style.backgroundColor = ''; // Restore default background color
    saveButton.style.cursor = ''; // Restore default cursor
    logo.disabled = false
    style.disabled = false
    size.disabled = false
    link.disabled = false
    color.disabled = false
    ccColor.disabled = false
    ecColor.disabled = false
    bcColor.disabled = false
}

function checkColorInputs() {
    const colorChoice = document.getElementById('color').value;
    if (colorChoice === 'custom') {
        enableColorInputs(); // Enable color inputs for custom colors
    } else {
        disableColorInputs(); // Disable color inputs for non-custom colors
        // console.log('done')
    }
}

// Event listener for logo selection
document.getElementById('logo').addEventListener('change', function () {
    const logo = this.value;
    const fileUploadRow = document.getElementById('fileUploadRow');
    const defaultOption = document.querySelector("#color option[value='default']");
    const colorDropdown = document.getElementById('color');

    // Toggle file input visibility for custom logo
    fileUploadRow.style.display = (logo === 'custom') ? 'flex' : 'none';

    // Show/hide default color option
    if (logo === 'none' || logo === 'custom') {
        if (defaultOption) {
            defaultOption.style.display = 'none';
            colorDropdown.selectedIndex = 0; // Set to a different option (like "No Color")

        }
    } else {
        if (defaultOption) {
            defaultOption.style.display = 'block';
            colorDropdown.selectedIndex = 2; // Show the default option
        }
    }

    // const colorChoice = document.getElementById('color').value;

    // Update color inputs based on selected logo
    updateColorInputs(logo)
    // if (colorChoice === 'custom') {
    //     enableColorInputs(); // Enable color inputs for custom colors
    // } else {
    //     disableColorInputs(); // Disable color inputs for non-custom colors
    //     console.log('done')
    // }



});

// Function to update color inputs based on selected logo
function updateColorInputs(logo) {
    const ccColorInput = document.getElementById('ccColor');
    const ecColorInput = document.getElementById('ecColor');
    const bcColorInput = document.getElementById('bcColor');
    const colorChoice = document.getElementById('color').value;

    // Set default colors based on selected logo
    let colors = defaultColors.default; // Default colors
    if (logo in defaultColors) {
        colors = defaultColors[logo]; // Get colors for the selected logo
        }
    if (colorChoice === 'none') {
        colors = defaultColors.default; // Default colors
    }

    ccColorInput.value = colors.cc; // Update center color
    ecColorInput.value = colors.ec; // Update edge color
    bcColorInput.value = colors.bc; // Update back color
    checkColorInputs()
}

// Function to toggle submit button state
// function toggleSubmitButton(button, isDisabled, text) {
//     button.disabled = isDisabled;  // Disable or enable the button
//     button.style.backgroundColor = isDisabled ? '#ccc' : ''; // Change background color
//     button.textContent = text; // Change button text
// }

// Function to validate hex color format
function validateHex(hex) {
    const hexColorPattern = /^#[0-9A-Fa-f]{6}$/; // Matches format #rrggbb
    return hexColorPattern.test(hex);
}

// Function to display the QR code image
function displayQRCode(item) {
    const qrCodeImage = document.getElementById('qrCodeImage');
    qrCodeImage.src = `data:image/png;base64,${item.qr_code_image}`; // Format base64 image
    qrCodeImage.style.display = 'block'; // Show the image
    enableSaveButton(); // Enable save button after QR code is generated

    // Show the save button
    const saveButton = document.getElementById('saveQRCodeButton');
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
// // Default back color initialization
// document.getElementById('bcColor').value = '#ffffff';

// Add an event listener to the color selection dropdown
document.getElementById('color').addEventListener('change', function () {
    // const colorChoice = this.value;
    // console.log(colorChoice)
    const logo = document.getElementById('logo').value;
    // let ccColorInput = document.getElementById('ccColor');
    // let ecColorInput = document.getElementById('ecColor');
    // let bcColorInput = document.getElementById('bcColor');

    // if (colorChoice === 'none') {
    //     // Reset colors when "No Color" is selected
    //     ccColorInput.value = '#000000'; // Default center color
    //     ecColorInput.value = '#000000'; // Default edge color
    //     bcColorInput.value = '#ffffff'; // Default back color
    //     disableColorInputs(); // Disable color inputs
    //     // console.log('disabled')
    // } else if (colorChoice === 'custom') {
    //     // Enable color inputs for custom color selection
    //     enableColorInputs(); // Enable color inputs
    //     // console.log('enabled')
    // } else {
    //     // Restore default colors based on the selected logo if "Default Color" is selected
    //     if (logo in defaultColors) {
    //         const selectedColors = defaultColors[logo];
    //         ccColorInput.value = selectedColors.cc;
    //         ecColorInput.value = selectedColors.ec;
    //         bcColorInput.value = selectedColors.bc;
    //     } else {
    //         // Fallback to default colors if logo is not in defaultColors
    //         ccColorInput.value = defaultColors.default.cc;
    //         ecColorInput.value = defaultColors.default.ec;
    //         bcColorInput.value = defaultColors.default.bc;
    //     }
    //     disableColorInputs(); // Disable color inputs for default colors
    //     // console.log('disabled')
    // }
    updateColorInputs(logo)
});

// Listen for the form submission event
document.getElementById('userForm').addEventListener('change', async function (event) {
    event.preventDefault();
    let formData = new FormData();
    disableSaveButton(); // Disable the save button while generating the QR code

    // Collect form data
    const logo = document.getElementById('logo').value;
    const link = document.getElementById('link').value;
    const cc = document.getElementById('ccColor').value;
    const ec = document.getElementById('ecColor').value;
    const bc = document.getElementById('bcColor').value;
    const style = document.getElementById('style').value;
    const size = document.getElementById('size').value;

    // Validate color inputs
    if (!validateHex(cc) || !validateHex(ec) || !validateHex(bc)) {
        alert("Please enter valid hex color codes (e.g., #rrggbb).");
        return;
    }

    // Add form fields to FormData object
    formData.append('logo', logo);
    formData.append('link', link);
    formData.append('cc', cc);
    formData.append('ec', ec);
    formData.append('bc', bc);
    formData.append('style', style);
    formData.append('size', size);

    // If a custom logo is selected, append the file to FormData
    if (logo === 'custom') {
        const logoFile = document.getElementById('logoFile').files[0];
        if (logoFile) {
            formData.append('logoFile', logoFile); // Append the logo file
        }
    }


    try {
        const response = await fetch('http://127.0.0.1:5000/', {
            method: 'POST',
            body: formData // No need to set Content-Type, let the browser do it
        });

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
