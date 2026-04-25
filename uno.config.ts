import { defineConfig } from 'unocss'

// Maps semantic shorthand tokens to our HSL CSS variables.
// Usage in Markdown: class="text-accent shadow-card"
// Because our CSS vars store raw HSL channel values (e.g., "25 95% 53%"),
// UnoCSS can automatically compose hsl(var(--accent-primary) / opacity) 
// for opacity-aware utilities.
export default defineConfig({
  theme: {
    colors: {
      'bg-primary':    'hsl(var(--bg-primary))',
      'bg-card':       'hsl(var(--bg-card))',
      'text-main':     'hsl(var(--text-main))',
      'border-main':   'hsl(var(--border-main))',
      'accent':        'hsl(var(--accent-primary))',
      'accent-sec':    'hsl(var(--accent-secondary))',
      'accent-tert':   'hsl(var(--accent-tertiary))',
    }
  },
  shortcuts: {
    // Utility shortcuts for common patterns in slide markdown
    'slide-card-shadow': 'shadow-[0_4px_15px_-3px_hsl(var(--text-main)/0.1)]',
    'neon-glow':         'shadow-[0_0_15px_hsl(var(--accent-secondary)/0.4)]',
    'subtle-border':     'border border-solid border-[hsl(var(--border-main)/0.3)]',
  }
})
