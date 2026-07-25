# CampusHub Design System Documentation

## Overview

This design system provides a complete foundation for building premium, modern UI components inspired by leading platforms like Threads, Discord, Linear, Notion, and Vercel.

**Version**: 1.0.0  
**Last Updated**: 2026-07-25

---

## Architecture

### CSS File Structure

```
static/css/
├── design-system.css  ← Design tokens & CSS variables (load first)
├── components.css     ← Reusable component library (load second)
└── style.css          ← Project-specific overrides (load last)
```

**Load Order in `base.html`:**
```html
<link rel="stylesheet" href="{% static 'css/design-system.css' %}">
<link rel="stylesheet" href="{% static 'css/components.css' %}">
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

---

## Design Tokens

### Typography

#### Font Families
```css
var(--font-sans)  /* System font stack for UI */
var(--font-mono)  /* Monospace for code */
```

#### Font Sizes
| Token | Size | Usage |
|-------|------|-------|
| `--text-xs` | 12px | Captions, labels |
| `--text-sm` | 14px | Secondary text |
| `--text-base` | 16px | Body text |
| `--text-lg` | 18px | Large body |
| `--text-xl` | 20px | Subheadings |
| `--text-2xl` | 24px | Card titles |
| `--text-3xl` | 32px | Page titles |
| `--text-4xl` | 40px | Hero text |
| `--text-5xl` | 48px | Large hero |
| `--text-6xl` | 64px | Extra large |

#### Font Weights
```css
var(--font-normal)    /* 400 */
var(--font-medium)    /* 500 */
var(--font-semibold)  /* 600 */
var(--font-bold)      /* 700 */
```

#### Line Heights
```css
var(--leading-none)     /* 1 */
var(--leading-tight)    /* 1.25 */
var(--leading-snug)     /* 1.375 */
var(--leading-normal)   /* 1.5 */
var(--leading-relaxed)  /* 1.75 */
var(--leading-loose)    /* 2 */
```

---

### Color System

#### Neutrals (Gray Scale)
```css
--color-white
--color-neutral-50   /* Lightest gray */
--color-neutral-100
--color-neutral-150
--color-neutral-200
--color-neutral-300
--color-neutral-400
--color-neutral-500  /* Mid gray */
--color-neutral-600
--color-neutral-700
--color-neutral-800
--color-neutral-900  /* Almost black */
--color-black
```

#### Brand Colors (Blue)
```css
--color-brand-50   /* Lightest */
--color-brand-500  /* Primary brand color */
--color-brand-600  /* Hover state */
--color-brand-700  /* Active state */
--color-brand-900  /* Darkest */
```

#### Semantic Colors
**Success (Green)**
```css
--color-success-50
--color-success-500
--color-success-600
--color-success-700
```

**Warning (Orange)**
```css
--color-warning-50
--color-warning-500
--color-warning-600
--color-warning-700
```

**Error (Red)**
```css
--color-error-50
--color-error-500
--color-error-600
--color-error-700
```

#### Semantic Tokens
```css
/* Backgrounds */
--bg-primary        /* White */
--bg-secondary      /* Light gray */
--bg-tertiary       /* Medium gray */
--bg-elevated       /* White with shadow */
--bg-brand          /* Brand color */

/* Text */
--text-primary      /* Dark gray (main text) */
--text-secondary    /* Medium gray */
--text-tertiary     /* Light gray */
--text-inverse      /* White (on dark bg) */
--text-brand        /* Brand color */

/* Borders */
--border-primary    /* Light border */
--border-secondary  /* Medium border */
--border-brand      /* Brand border */
```

---

### Spacing Scale (8px Base)

```css
--space-0   /* 0px */
--space-1   /* 4px */
--space-2   /* 8px */
--space-3   /* 12px */
--space-4   /* 16px */
--space-5   /* 20px */
--space-6   /* 24px */
--space-8   /* 32px */
--space-10  /* 40px */
--space-12  /* 48px */
--space-16  /* 64px */
--space-20  /* 80px */
--space-24  /* 96px */
--space-32  /* 128px */
```

**Usage:**
```html
<div style="padding: var(--space-6);">Content</div>
<div style="gap: var(--space-4);">Items</div>
```

---

### Shadows

```css
--shadow-xs    /* Subtle shadow */
--shadow-sm    /* Small shadow */
--shadow-md    /* Medium shadow */
--shadow-lg    /* Large shadow */
--shadow-xl    /* Extra large */
--shadow-2xl   /* Maximum shadow */
--shadow-inner /* Inset shadow */
--shadow-glow  /* Focus glow (brand) */
```

**Examples:**
```css
.card { box-shadow: var(--shadow-sm); }
.elevated { box-shadow: var(--shadow-md); }
input:focus { box-shadow: var(--shadow-glow); }
```

---

### Border Radius

```css
--radius-sm    /* 6px */
--radius-md    /* 8px */
--radius-lg    /* 12px */
--radius-xl    /* 16px */
--radius-2xl   /* 24px */
--radius-3xl   /* 32px */
--radius-full  /* Circle/pill */
```

---

### Transitions

```css
--transition-fast    /* 150ms - buttons, hover */
--transition-base    /* 200ms - general */
--transition-slow    /* 300ms - complex */
--transition-spring  /* 400ms - bouncy effects */
```

**Usage:**
```css
.button {
  transition: all var(--transition-fast);
}
```

---

## Component Library

### Buttons

#### Button Variants
```html
<!-- Primary (dark) -->
<button class="btn btn-md btn-primary">Primary Button</button>

<!-- Brand (blue) -->
<button class="btn btn-md btn-brand">Brand Button</button>

<!-- Secondary (gray) -->
<button class="btn btn-md btn-secondary">Secondary</button>

<!-- Outline -->
<button class="btn btn-md btn-outline">Outline</button>

<!-- Ghost -->
<button class="btn btn-md btn-ghost">Ghost</button>

<!-- Danger -->
<button class="btn btn-md btn-danger">Delete</button>

<!-- Link style -->
<button class="btn btn-link">Link Button</button>
```

#### Button Sizes
```html
<button class="btn btn-xs">Extra Small</button>
<button class="btn btn-sm">Small</button>
<button class="btn btn-md">Medium</button>
<button class="btn btn-lg">Large</button>
<button class="btn btn-xl">Extra Large</button>
```

#### Button States
```html
<!-- Disabled -->
<button class="btn btn-primary" disabled>Disabled</button>

<!-- Loading -->
<button class="btn btn-primary btn-loading">Loading...</button>

<!-- Full Width -->
<button class="btn btn-primary btn-full">Full Width</button>

<!-- Icon Only -->
<button class="btn btn-primary btn-icon-only">
  <svg>...</svg>
</button>
```

#### Button with Icons
```html
<button class="btn btn-primary">
  <svg class="w-4 h-4">...</svg>
  <span>Button Text</span>
</button>
```

---

### Inputs

#### Text Input
```html
<div class="input-group">
  <label class="input-label">Email Address</label>
  <input type="email" class="input input-md" placeholder="you@example.com">
  <span class="input-helper">We'll never share your email.</span>
</div>
```

#### Input Sizes
```html
<input type="text" class="input input-sm" placeholder="Small">
<input type="text" class="input input-md" placeholder="Medium">
<input type="text" class="input input-lg" placeholder="Large">
```

#### Input States
```html
<!-- Default -->
<input type="text" class="input">

<!-- Error -->
<input type="text" class="input input-error">
<span class="input-error-message">This field is required</span>

<!-- Success -->
<input type="text" class="input input-success">

<!-- Disabled -->
<input type="text" class="input" disabled>
```

#### Textarea
```html
<div class="input-group">
  <label class="input-label">Description</label>
  <textarea class="textarea" rows="4" placeholder="Enter description..."></textarea>
</div>
```

#### Select Dropdown
```html
<div class="input-group">
  <label class="input-label">Category</label>
  <select class="select select-md">
    <option>Select option</option>
    <option>Option 1</option>
    <option>Option 2</option>
  </select>
</div>
```

#### File Input
```html
<input type="file" class="input input-file">
```

---

### Cards

#### Basic Card
```html
<div class="card">
  <div class="card-body">
    <h3>Card Title</h3>
    <p>Card content goes here.</p>
  </div>
</div>
```

#### Card with Header & Footer
```html
<div class="card">
  <div class="card-header">
    <h3>Card Header</h3>
  </div>
  <div class="card-body">
    <p>Main content</p>
  </div>
  <div class="card-footer">
    <button class="btn btn-primary">Action</button>
  </div>
</div>
```

#### Card Variants
```html
<!-- Flat (no shadow) -->
<div class="card card-flat">...</div>

<!-- Elevated (more shadow) -->
<div class="card card-elevated">...</div>

<!-- Interactive (hover effect) -->
<a href="#" class="card card-interactive">...</a>

<!-- Glassmorphism -->
<div class="card card-glass">...</div>
```

#### Card with Image
```html
<div class="card card-interactive">
  <img src="image.jpg" alt="Post" class="card-image">
  <div class="card-body">
    <h3>Card Title</h3>
    <p>Description</p>
  </div>
</div>
```

---

### Badges

```html
<!-- Variants -->
<span class="badge badge-neutral">Neutral</span>
<span class="badge badge-brand">Brand</span>
<span class="badge badge-success">Success</span>
<span class="badge badge-warning">Warning</span>
<span class="badge badge-error">Error</span>

<!-- Sizes -->
<span class="badge badge-sm">Small</span>
<span class="badge">Default</span>
<span class="badge badge-lg">Large</span>

<!-- With Dot -->
<span class="badge badge-success badge-dot">Active</span>
```

---

### Avatars

```html
<!-- Sizes -->
<div class="avatar avatar-xs">
  <img src="profile.jpg" alt="User" class="avatar-img">
</div>
<div class="avatar avatar-sm">...</div>
<div class="avatar avatar-md">...</div>
<div class="avatar avatar-lg">...</div>
<div class="avatar avatar-xl">...</div>
<div class="avatar avatar-2xl">...</div>

<!-- With Initials (no image) -->
<div class="avatar avatar-md">
  <span>JD</span>
</div>

<!-- With Ring -->
<div class="avatar avatar-md avatar-ring">...</div>

<!-- Square -->
<div class="avatar avatar-md avatar-square">...</div>
```

---

### Loading States

#### Spinner
```html
<div class="spinner"></div>
<div class="spinner spinner-sm"></div>
<div class="spinner spinner-lg"></div>
```

#### Skeleton Loaders
```html
<!-- Text skeleton -->
<div class="skeleton skeleton-text"></div>

<!-- Title skeleton -->
<div class="skeleton skeleton-title"></div>

<!-- Circle skeleton (avatar) -->
<div class="skeleton skeleton-circle"></div>

<!-- Button skeleton -->
<div class="skeleton skeleton-button"></div>

<!-- Custom skeleton -->
<div class="skeleton" style="height: 200px; width: 100%;"></div>
```

---

### Utility Classes

#### Text Utilities
```html
<p class="truncate">This text will be truncated...</p>
<p class="line-clamp-1">Single line clamp</p>
<p class="line-clamp-2">Two line clamp</p>
<p class="line-clamp-3">Three line clamp</p>
<p class="gradient-text">Gradient text</p>
```

#### Layout Utilities
```html
<div class="container">Centered container</div>
<div class="aspect-video">16:9 aspect ratio</div>
<div class="aspect-square">1:1 aspect ratio</div>
```

#### Visibility Utilities
```html
<div class="hide-mobile">Hidden on mobile</div>
<div class="hide-desktop">Hidden on desktop</div>
<div class="show-mobile">Only on mobile</div>
<span class="sr-only">Screen reader only</span>
```

#### Glassmorphism
```html
<div class="glass">Glassmorphic background</div>
<div class="glass-dark">Dark glassmorphic</div>
```

#### Animation Utilities
```html
<div class="animate-fade-in">Fade in</div>
<div class="animate-slide-up">Slide up</div>
<div class="animate-scale-in">Scale in</div>
<div class="animate-pulse">Pulse</div>
<button class="ripple">Ripple effect</button>
```

---

## Usage Examples

### Form Example
```html
<form class="card">
  <div class="card-body" style="display: flex; flex-direction: column; gap: var(--space-6);">
    <h2 style="font-size: var(--text-2xl); font-weight: var(--font-semibold); color: var(--text-primary);">
      Create Account
    </h2>
    
    <div class="input-group">
      <label class="input-label input-label-required">Full Name</label>
      <input type="text" class="input input-md" placeholder="John Doe">
    </div>
    
    <div class="input-group">
      <label class="input-label input-label-required">Email</label>
      <input type="email" class="input input-md" placeholder="you@example.com">
      <span class="input-helper">We'll never share your email.</span>
    </div>
    
    <div class="input-group">
      <label class="input-label">Bio</label>
      <textarea class="textarea" placeholder="Tell us about yourself..." rows="4"></textarea>
    </div>
    
    <button type="submit" class="btn btn-brand btn-lg btn-full">
      Create Account
    </button>
  </div>
</form>
```

### Post Card Example
```html
<a href="/posts/123" class="card card-interactive">
  <img src="post.jpg" alt="Post" class="card-image" style="aspect-ratio: 16/9; object-fit: cover;">
  
  <div class="card-body" style="display: flex; flex-direction: column; gap: var(--space-3);">
    <span class="badge badge-brand">Roommate</span>
    
    <h3 class="line-clamp-2" style="font-size: var(--text-lg); font-weight: var(--font-semibold);">
      Looking for roommate near campus
    </h3>
    
    <p class="line-clamp-3" style="font-size: var(--text-sm); color: var(--text-secondary);">
      Description of the post goes here...
    </p>
    
    <div style="display: flex; align-items: center; gap: var(--space-4); font-size: var(--text-xs); color: var(--text-tertiary);">
      <span>📍 Mumbai</span>
      <span>⏰ 2h ago</span>
    </div>
  </div>
</a>
```

---

## Best Practices

### 1. **Use Design Tokens**
❌ Don't use hardcoded values:
```css
.button {
  padding: 12px 20px;
  border-radius: 8px;
  color: #171717;
}
```

✅ Use design tokens:
```css
.button {
  padding: var(--space-3) var(--space-5);
  border-radius: var(--radius-lg);
  color: var(--text-primary);
}
```

### 2. **Consistent Spacing**
Always use the 8px spacing scale:
- Small gaps: `var(--space-2)` or `var(--space-3)`
- Medium gaps: `var(--space-4)` or `var(--space-6)`
- Large gaps: `var(--space-8)` or `var(--space-12)`

### 3. **Semantic Color Usage**
- Use `--text-primary` for main text
- Use `--text-secondary` for less important text
- Use `--text-tertiary` for captions
- Use `--text-brand` for links and accents

### 4. **Component Classes**
Prefer component classes over custom styles:
```html
<!-- ❌ Custom styling -->
<button style="background: blue; padding: 12px;">Click</button>

<!-- ✅ Component class -->
<button class="btn btn-brand btn-md">Click</button>
```

### 5. **Responsive Design**
Mobile-first approach:
```css
/* Mobile first */
.element {
  padding: var(--space-4);
}

/* Desktop enhancement */
@media (min-width: 768px) {
  .element {
    padding: var(--space-6);
  }
}
```

---

## Migration Guide

### Updating Existing Components

**Before:**
```html
<button class="bg-blue-500 text-white px-6 py-3 rounded-lg hover:bg-blue-600">
  Submit
</button>
```

**After:**
```html
<button class="btn btn-brand btn-md">
  Submit
</button>
```

**Before:**
```html
<input type="text" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2">
```

**After:**
```html
<input type="text" class="input input-md">
```

---

## Browser Support

- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support  
- Safari: ✅ Full support (with autoprefixer)
- Mobile browsers: ✅ Full support

CSS Features Used:
- CSS Custom Properties (variables)
- Flexbox
- Grid (where needed)
- CSS Animations
- Backdrop filters (for glassmorphism)

---

## Performance

- **File Size**: ~25KB combined (design-system + components + style)
- **No JavaScript Dependencies**: Pure CSS
- **GPU Accelerated**: Transforms and opacity for animations
- **Mobile Optimized**: Mobile-first approach

---

## Future Enhancements

- [ ] Dark mode support (CSS variables prepared)
- [ ] RTL language support
- [ ] Additional component variants
- [ ] Animation library expansion
- [ ] Accessibility improvements
- [ ] Print stylesheets

---

## Support & Contribution

For questions or suggestions about the design system:
1. Review this documentation
2. Check existing components in `components.css`
3. Follow established patterns
4. Maintain consistency with design tokens

---

**CampusHub Design System v1.0.0**  
Built for premium, modern, and accessible UI experiences.
