# Images Directory Structure

This directory contains all the images used in the Living Meaningful Life website.

## 📁 Directory Structure

```
public/images/
├── hero/           # Hero section slideshow images
├── events/         # Event photos and thumbnails
├── alumni/         # Alumni profile pictures
├── icons/          # Custom icons and logos
└── README.md       # This file
```

## 🖼️ Image Guidelines

### Hero Section Images
- **Location**: `public/images/hero/`
- **Naming**: `hero-1.jpg`, `hero-2.jpg`, etc.
- **Size**: 1920x1080px (16:9 aspect ratio)
- **Format**: JPG or PNG
- **Theme**: Education, community, wisdom, collaboration

### Event Images
- **Location**: `public/images/events/`
- **Naming**: `event-name.jpg` (e.g., `mera-bharat-mahan.jpg`)
- **Size**: 800x600px (4:3 aspect ratio)
- **Format**: JPG or PNG

### Alumni Photos
- **Location**: `public/images/alumni/`
- **Naming**: `firstname-lastname.jpg` (e.g., `vishal-kaushal.jpg`)
- **Size**: 400x400px (1:1 aspect ratio - square)
- **Format**: JPG or PNG
- **Style**: Professional headshots

### Icons & Logos
- **Location**: `public/images/icons/`
- **Naming**: Descriptive names (e.g., `logo.png`, `bhagavad-gita-symbol.png`)
- **Size**: Various (SVG preferred for scalability)
- **Format**: SVG, PNG, or ICO

## 🎨 Image Optimization Tips

1. **Compress images** before adding them to reduce file size
2. **Use appropriate formats**: JPG for photos, PNG for graphics with transparency
3. **Maintain consistent aspect ratios** within each category
4. **Use descriptive filenames** for easy identification

## 📝 How to Add New Images

1. **Place the image** in the appropriate directory
2. **Update the code** in `src/App.js` to reference the new image
3. **Test the website** to ensure the image displays correctly

## 🔄 Replacing Images

To replace an existing image:
1. **Keep the same filename** to avoid code changes
2. **Or update the filename** in `src/App.js` if you change the name
3. **Maintain the same dimensions** for consistency 