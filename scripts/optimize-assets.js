import fs from 'fs';
import path from 'path';
import sharp from 'sharp';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const publicDir = path.join(__dirname, '../public');

if (!fs.existsSync(publicDir)) {
  console.log('❌ Public directory not found. Create a public/ folder for your images.');
  process.exit(0);
}

const files = fs.readdirSync(publicDir);
let optimizedCount = 0;

(async () => {
  console.log('🚀 Starting Asset Optimization...');
  
  for (const file of files) {
    const ext = path.extname(file).toLowerCase();
    
    // Only process png, jpg, jpeg
    if (['.png', '.jpg', '.jpeg'].includes(ext)) {
      const filePath = path.join(publicDir, file);
      const newFileName = file.replace(new RegExp(`${ext}$`), '.webp');
      const newFilePath = path.join(publicDir, newFileName);
      
      try {
        console.log(`⏳ Optimizing: ${file} -> ${newFileName}`);
        
        await sharp(filePath)
          .webp({ quality: 80 })
          .toFile(newFilePath);
          
        // Get sizes for comparison
        const oldSize = fs.statSync(filePath).size;
        const newSize = fs.statSync(newFilePath).size;
        const savings = ((oldSize - newSize) / oldSize * 100).toFixed(1);
        
        console.log(`✅ Optimized ${newFileName} | Saved ${savings}% space.`);
        
        // Delete original to save space
        fs.unlinkSync(filePath);
        optimizedCount++;
      } catch (err) {
        console.error(`❌ Failed to optimize ${file}:`, err.message);
      }
    }
  }
  
  console.log(`\n🎉 Optimization Complete! Processed ${optimizedCount} images.`);
  if (optimizedCount > 0) {
    console.log('⚠️ IMPORTANT: Don\'t forget to update your markdown files to reference the new .webp extensions!');
  }
})();
