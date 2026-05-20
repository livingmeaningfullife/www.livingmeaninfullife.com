# Image Instructions for Living Meaningful Life Website

## 📸 How to Add Images

### 🎯 **Quick Start**
1. **Add your images** to the appropriate folders below
2. **Name them correctly** following the naming conventions
3. **Update the code** in `src/App.js` to reference your images

### 📁 **Folder Structure**

```
public/images/
├── hero/           # Hero section slideshow (4 images)
├── events/         # Event photos (as many as needed)
├── alumni/         # Alumni profile pictures (as many as needed)
└── icons/          # Logos and custom icons
```

### 🖼️ **Image Requirements**

#### **Hero Section Images** (`hero/`)
- **Filenames**: `hero-1.jpg`, `hero-2.jpg`, `hero-3.jpg`, `hero-4.jpg`
- **Size**: 1920x1080px (Full HD, 16:9 ratio)
- **Theme**: Education, community, wisdom, spiritual growth
- **Format**: JPG (for smaller file size)

#### **Event Images** (`events/`)
- **Filenames**: Use event name (e.g., `mera-bharat-mahan.jpg`)
- **Size**: 800x600px (4:3 ratio)
- **Format**: JPG or PNG
- **Examples**:
  - `mera-bharat-mahan.jpg`
  - `mind-your-mind.jpg`
  - `ml-course-lml.jpg`
  - `power-of-habits.jpg`

#### **Alumni Photos** (`alumni/`)
- **Filenames**: `firstname-lastname.jpg` (e.g., `vishal-kaushal.jpg`)
- **Size**: 400x400px (Square, 1:1 ratio)
- **Format**: JPG
- **Style**: Professional headshots with good lighting
- **Examples**:
  - `vishal-kaushal.jpg`
  - `sandesh-borgaonkar.jpg`
  - `sai-praveen-kadiyala.jpg`

#### **Icons & Logos** (`icons/`)
- **Filenames**: Descriptive names
- **Format**: PNG (for transparency) or SVG (for scalability)
- **Examples**:
  - `logo.png`
  - `bhagavad-gita-symbol.png`
  - `lotus-icon.svg`

### 🔧 **After Adding Images**

1. **Update the code** in `src/App.js`:
   - Find the relevant array (heroImages, events, alumni)
   - Update the `image` field with your filename
   - Save the file

2. **Test your website**:
   - Run `npm run dev`
   - Check if images load correctly
   - Test on mobile view

### 📝 **Example Code Updates**

#### For Hero Images:
```javascript
const heroImages = [
  {
    url: "/images/hero/hero-1.jpg",  // ← Your new image
    title: "Excellence in Education"
  },
  // ... add more
];
```

#### For Events:
```javascript
{
  title: "Your Event Name",
  image: "/images/events/your-event-name.jpg"  // ← Your new image
}
```

#### For Alumni:
```javascript
{
  name: "Alumni Name",
  image: "/images/alumni/firstname-lastname.jpg"  // ← Your new image
}
```

### 🎨 **Image Tips**

1. **Optimize images** before uploading (compress to reduce file size)
2. **Use consistent lighting** for alumni photos
3. **Choose high-quality** images that represent the spiritual theme
4. **Maintain aspect ratios** for consistent layout
5. **Use descriptive filenames** for easy management

### 🚨 **Common Issues**

- **Image not showing?** Check the filename and path
- **Image too large?** Compress it or resize to recommended dimensions
- **Wrong aspect ratio?** Crop/resize to match requirements
- **File format issues?** Use JPG for photos, PNG for graphics with transparency

### 📞 **Need Help?**

If images aren't working:
1. Check browser console (F12) for error messages
2. Verify file paths and names match exactly
3. Ensure images are in the correct folders
4. Ask for help in the community group 