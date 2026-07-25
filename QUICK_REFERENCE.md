# Design System Quick Reference

Quick copy-paste examples for common UI patterns.

---

## Buttons

```html
<!-- Primary actions -->
<button class="btn btn-md btn-primary">Primary</button>
<button class="btn btn-md btn-brand">Brand Blue</button>

<!-- Secondary actions -->
<button class="btn btn-md btn-secondary">Secondary</button>
<button class="btn btn-md btn-outline">Outline</button>
<button class="btn btn-md btn-ghost">Ghost</button>

<!-- Destructive actions -->
<button class="btn btn-md btn-danger">Delete</button>

<!-- Sizes -->
<button class="btn btn-sm btn-brand">Small</button>
<button class="btn btn-md btn-brand">Medium</button>
<button class="btn btn-lg btn-brand">Large</button>

<!-- Full width -->
<button class="btn btn-md btn-brand btn-full">Full Width</button>

<!-- With icon -->
<button class="btn btn-md btn-brand">
  <svg class="w-4 h-4">...</svg>
  <span>Text</span>
</button>
```

---

## Inputs

```html
<!-- Text input -->
<div class="input-group">
  <label class="input-label">Label</label>
  <input type="text" class="input input-md" placeholder="Placeholder">
  <span class="input-helper">Helper text</span>
</div>

<!-- Required field -->
<label class="input-label input-label-required">Required Field</label>

<!-- With error -->
<input type="text" class="input input-md input-error" value="Invalid">
<span class="input-error-message">❌ Error message</span>

<!-- Textarea -->
<textarea class="textarea" rows="4" placeholder="Enter text..."></textarea>

<!-- Select -->
<select class="select select-md">
  <option>Option 1</option>
  <option>Option 2</option>
</select>

<!-- File upload -->
<input type="file" class="input input-file">
```

---

## Cards

```html
<!-- Basic card -->
<div class="card">
  <div class="card-body">
    Content
  </div>
</div>

<!-- Card with header -->
<div class="card">
  <div class="card-header">
    <h3>Header</h3>
  </div>
  <div class="card-body">
    Content
  </div>
</div>

<!-- Interactive card (clickable) -->
<a href="#" class="card card-interactive">
  <div class="card-body">
    Clickable content
  </div>
</a>

<!-- Post card pattern -->
<div class="card card-interactive">
  <img src="image.jpg" alt="Post" class="card-image">
  <div class="card-body">
    <span class="badge badge-brand">Category</span>
    <h3 class="line-clamp-2">Title</h3>
    <p class="line-clamp-3">Description</p>
  </div>
</div>
```

---

## Badges

```html
<!-- Color variants -->
<span class="badge badge-neutral">Neutral</span>
<span class="badge badge-brand">Brand</span>
<span class="badge badge-success">Success</span>
<span class="badge badge-warning">Warning</span>
<span class="badge badge-error">Error</span>

<!-- With dot indicator -->
<span class="badge badge-success badge-dot">Active</span>
<span class="badge badge-error badge-dot">Expired</span>
```

---

## Avatars

```html
<!-- With initials -->
<div class="avatar avatar-md">
  <span>JD</span>
</div>

<!-- With image -->
<div class="avatar avatar-md">
  <img src="profile.jpg" alt="User" class="avatar-img">
</div>

<!-- Sizes -->
<div class="avatar avatar-sm">...</div>
<div class="avatar avatar-md">...</div>
<div class="avatar avatar-lg">...</div>
```

---

## Loading States

```html
<!-- Spinner -->
<div class="spinner"></div>

<!-- Button loading -->
<button class="btn btn-md btn-brand btn-loading">Loading</button>

<!-- Skeleton (card loading) -->
<div class="card">
  <div class="card-body">
    <div class="skeleton skeleton-title"></div>
    <div class="skeleton skeleton-text"></div>
    <div class="skeleton skeleton-text"></div>
    <div class="skeleton skeleton-button"></div>
  </div>
</div>
```

---

## Layout Patterns

```html
<!-- Centered container -->
<div class="container">
  Content
</div>

<!-- Flex row with gap -->
<div style="display: flex; gap: var(--space-4);">
  <div>Item 1</div>
  <div>Item 2</div>
</div>

<!-- Flex column with gap -->
<div style="display: flex; flex-direction: column; gap: var(--space-6);">
  <div>Item 1</div>
  <div>Item 2</div>
</div>

<!-- Grid -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: var(--space-6);">
  <div>Card 1</div>
  <div>Card 2</div>
  <div>Card 3</div>
</div>
```

---

## Typography

```html
<!-- Headings -->
<h1 style="font-size: var(--text-4xl); font-weight: var(--font-bold);">
  Page Title
</h1>
<h2 style="font-size: var(--text-3xl); font-weight: var(--font-semibold);">
  Section Title
</h2>
<h3 style="font-size: var(--text-2xl); font-weight: var(--font-semibold);">
  Card Title
</h3>

<!-- Body text -->
<p style="font-size: var(--text-base); color: var(--text-primary);">
  Body text
</p>
<p style="font-size: var(--text-sm); color: var(--text-secondary);">
  Secondary text
</p>
<p style="font-size: var(--text-xs); color: var(--text-tertiary);">
  Caption text
</p>

<!-- Text utilities -->
<p class="truncate">This text will truncate...</p>
<p class="line-clamp-2">This text will clamp to 2 lines...</p>
```

---

## Common Design Tokens

```css
/* Spacing (use in inline styles or custom CSS) */
padding: var(--space-4);         /* 16px */
gap: var(--space-6);              /* 24px */
margin-bottom: var(--space-8);    /* 32px */

/* Colors */
color: var(--text-primary);       /* Main text */
color: var(--text-secondary);     /* Secondary text */
color: var(--text-brand);         /* Brand color */
background: var(--bg-primary);    /* White */
background: var(--bg-secondary);  /* Light gray */

/* Border */
border: var(--border-width-1) solid var(--border-primary);
border-radius: var(--radius-lg);  /* 12px */

/* Shadow */
box-shadow: var(--shadow-sm);     /* Small shadow */
box-shadow: var(--shadow-md);     /* Medium shadow */

/* Transitions */
transition: all var(--transition-fast);  /* 150ms */
```

---

## Responsive Patterns

```html
<!-- Hide on mobile -->
<div class="hide-mobile">Desktop only</div>

<!-- Hide on desktop -->
<div class="hide-desktop">Mobile only</div>

<!-- Responsive grid -->
<div style="display: grid; grid-template-columns: 1fr; gap: var(--space-4);">
  <!-- Mobile: 1 column, Tablet+: Use media queries -->
</div>

@media (min-width: 768px) {
  /* Tablet and up */
  .my-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  /* Desktop */
  .my-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

---

## Form Pattern

```html
<form class="card">
  <div class="card-body" style="display: flex; flex-direction: column; gap: var(--space-6);">
    
    <h2 style="font-size: var(--text-2xl); font-weight: var(--font-semibold);">
      Form Title
    </h2>
    
    <div class="input-group">
      <label class="input-label input-label-required">Name</label>
      <input type="text" class="input input-md" placeholder="Enter name">
    </div>
    
    <div class="input-group">
      <label class="input-label">Email</label>
      <input type="email" class="input input-md" placeholder="you@example.com">
      <span class="input-helper">We'll never share your email</span>
    </div>
    
    <div class="input-group">
      <label class="input-label">Category</label>
      <select class="select select-md">
        <option>Select...</option>
        <option>Option 1</option>
      </select>
    </div>
    
    <div class="input-group">
      <label class="input-label">Description</label>
      <textarea class="textarea" rows="4" placeholder="Enter description"></textarea>
    </div>
    
    <div style="display: flex; gap: var(--space-3);">
      <button type="submit" class="btn btn-brand btn-md btn-full">
        Submit
      </button>
      <button type="button" class="btn btn-secondary btn-md">
        Cancel
      </button>
    </div>
    
  </div>
</form>
```

---

## Post Card Pattern

```html
<a href="/posts/123" class="card card-interactive">
  <!-- Image -->
  <img src="post.jpg" alt="Post" class="card-image" style="aspect-ratio: 16/9; object-fit: cover;">
  
  <!-- Content -->
  <div class="card-body" style="display: flex; flex-direction: column; gap: var(--space-3);">
    
    <!-- Category badge -->
    <span class="badge badge-brand">Roommate</span>
    
    <!-- Title -->
    <h3 class="line-clamp-2" style="font-size: var(--text-lg); font-weight: var(--font-semibold); color: var(--text-primary);">
      Looking for roommate near campus
    </h3>
    
    <!-- Description -->
    <p class="line-clamp-3" style="font-size: var(--text-sm); color: var(--text-secondary);">
      Description text goes here. This will be clamped to 3 lines.
    </p>
    
    <!-- Meta info -->
    <div style="display: flex; align-items: center; gap: var(--space-4); font-size: var(--text-xs); color: var(--text-tertiary);">
      <span>📍 Mumbai</span>
      <span>⏰ 2h ago</span>
    </div>
    
    <!-- Price (if exists) -->
    <div style="font-size: var(--text-xl); font-weight: var(--font-bold); color: var(--text-brand);">
      ₹5,000
    </div>
    
    <!-- Expiry badge -->
    <span class="badge badge-warning badge-sm">Expires in 5 days</span>
    
  </div>
</a>
```

---

## Empty State Pattern

```html
<div class="empty-state">
  <svg class="empty-state-icon">
    <!-- Icon SVG -->
  </svg>
  <h3 style="font-size: var(--text-xl); font-weight: var(--font-semibold); color: var(--text-primary); margin-bottom: var(--space-2);">
    No posts yet
  </h3>
  <p style="font-size: var(--text-base); color: var(--text-secondary); margin-bottom: var(--space-6);">
    Be the first to create a post.
  </p>
  <button class="btn btn-brand btn-lg">
    Create First Post
  </button>
</div>
```

---

## Profile Header Pattern

```html
<div class="card">
  <div class="card-body" style="display: flex; flex-direction: column; gap: var(--space-6);">
    
    <!-- Avatar + Name -->
    <div style="display: flex; align-items: center; gap: var(--space-4);">
      <div class="avatar avatar-xl">
        <img src="profile.jpg" alt="User" class="avatar-img">
      </div>
      <div>
        <h2 style="font-size: var(--text-2xl); font-weight: var(--font-semibold);">
          John Doe
        </h2>
        <p style="font-size: var(--text-sm); color: var(--text-secondary);">
          @johndoe
        </p>
      </div>
    </div>
    
    <!-- Bio -->
    <p style="font-size: var(--text-base); color: var(--text-primary);">
      Bio text goes here...
    </p>
    
    <!-- Stats -->
    <div style="display: flex; gap: var(--space-6);">
      <div>
        <div style="font-size: var(--text-2xl); font-weight: var(--font-bold); color: var(--text-brand);">
          24
        </div>
        <div style="font-size: var(--text-xs); color: var(--text-tertiary);">
          Posts
        </div>
      </div>
    </div>
    
    <!-- Actions -->
    <button class="btn btn-brand btn-md btn-full">
      Edit Profile
    </button>
    
  </div>
</div>
```

---

## Common Spacing Values

```
--space-1:  4px   ← Tiny gap
--space-2:  8px   ← Small gap
--space-3:  12px  ← Medium-small gap
--space-4:  16px  ← Standard gap ⭐
--space-5:  20px  ← Medium gap
--space-6:  24px  ← Large gap ⭐
--space-8:  32px  ← Extra large gap ⭐
--space-12: 48px  ← Section spacing
--space-16: 64px  ← Page spacing
```

⭐ = Most commonly used

---

## Color Usage Guide

```css
/* Text colors */
--text-primary      /* Main content text */
--text-secondary    /* Less important text */
--text-tertiary     /* Labels, captions */
--text-inverse      /* White text on dark bg */
--text-brand        /* Links, accents */

/* Background colors */
--bg-primary        /* White */
--bg-secondary      /* Light gray (page bg) */
--bg-tertiary       /* Medium gray */
--bg-elevated       /* White with shadow */

/* Border colors */
--border-primary    /* Light border */
--border-secondary  /* Medium border */
```

---

For complete documentation, see **DESIGN_SYSTEM.md**
