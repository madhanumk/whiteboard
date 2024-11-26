// Initialize Fabric.js canvas
const canvas = new fabric.Canvas('fabricCanvas', {
    isDrawingMode: true, // Enable drawing mode
});

// Brush settings
const colorPicker = document.getElementById('colorPicker');
const brushSize = document.getElementById('brushSize');
const clearCanvas = document.getElementById('clearCanvas');

// Set initial brush options
canvas.freeDrawingBrush.color = colorPicker.value;
canvas.freeDrawingBrush.width = parseInt(brushSize.value, 10);

// Update brush color
colorPicker.addEventListener('input', (e) => {
    canvas.freeDrawingBrush.color = e.target.value;
});

// Update brush size
brushSize.addEventListener('input', (e) => {
    canvas.freeDrawingBrush.width = parseInt(e.target.value, 10);
});

// Clear the canvas
clearCanvas.addEventListener('click', () => {
    canvas.clear(); // Clear all drawings
    // Reinitialize canvas options if needed
    canvas.isDrawingMode = true;
});
