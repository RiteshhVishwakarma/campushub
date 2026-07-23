# UI/UX Polish - Premium Design System

## Overview
Complete UI overhaul following Airbnb + Notion + Linear design principles with mobile-first, minimal, premium aesthetics.

## Design System - 8px Spacing

### Colors
```
Primary Blue:
- 50:  #eff6ff (Backgrounds)
- 100: #dbeafe (Hover states)
- 500: #3b82f6 (Primary actions)
- 600: #2563eb (Hover primary)
- 700: #1d4ed8 (Active primary)

Neutral Grays:
- 50:  #fafafa (Page background)
- 100: #f5f5f5 (Card backgrounds)
- 150: #f0f0f0 (Subtle borders)
- 200: #e5e5e5 (Borders)
- 300: #d4d4d4 (Dividers)
- 400: #a3a3a3 (Placeholder text)
- 500: #737373 (Secondary text)
- 600: #525252 (Body text)
- 700: #404040 (Headings)
- 900: #171717 (Heavy text)
```

### Typography
```
Font sizes (with line heights):
- xs:   0.75rem / 1rem     (12px/16px)
- sm:   0.875rem / 1.25rem (14px/20px)
- base: 1rem / 1.5rem      (16px/24px)
- lg:   1.125rem / 1.75rem (18px/28px)
- xl:   1.25rem / 1.75rem  (20px/28px)
- 2xl:  1.5rem / 2rem      (24px/32px)
- 3xl:  1.875rem / 2.25rem (30px/36px)

Weights:
- normal:   400
- medium:   500
- semibold: 600
- bold:     700
```

### Spacing (8px system)
```
0:    0px
1:    0.25rem  (4px)
2:    0.5rem   (8px)  ← Base unit
3:    0.75rem  (12px)
4:    1rem     (16px)
5:    1.25rem  (20px)
6:    1.5rem   (24px)
8:    2rem     (32px)
10:   2.5rem   (40px)
12:   3rem     (48px)
16:   4rem     (64px)
```

### Border Radius
```
sm:  0.375rem (6px)
md:  0.5rem   (8px)  ← Default
lg:  0.75rem  (12px)
xl:  1rem     (16px)
2xl: 1.5rem   (24px)
```

### Shadows
```
Minimal shadows only:
- sm:  0 1px 2px rgba(0,0,0,0.05)
- md:  0 1px 3px rgba(0,0,0,0.05)
- lg:  0 4px 6px rgba(0,0,0,0.05)
```

## Component Patterns

### Buttons
```html
<!-- Primary Button -->
<button class="inline-flex items-center gap-2 px-4 py-2.5 bg-primary-500 text-white text-sm font-medium rounded-lg hover:bg-primary-600 transition-colors">
    <svg class="w-4 h-4">...</svg>
    Button Text
</button>

<!-- Secondary Button -->
<button class="inline-flex items-center gap-2 px-4 py-2.5 bg-neutral-100 text-neutral-700 text-sm font-medium rounded-lg hover:bg-neutral-200 transition-colors">
    Button Text
</button>

<!-- Ghost Button -->
<button class="inline-flex items-center gap-2 px-4 py-2.5 text-neutral-700 text-sm font-medium rounded-lg hover:bg-neutral-100 transition-colors">
    Button Text
</button>

<!-- Destructive Button -->
<button class="inline-flex items-center gap-2 px-4 py-2.5 bg-red-500 text-white text-sm font-medium rounded-lg hover:bg-red-600 transition-colors">
    Delete
</button>
```

### Cards
```html
<!-- Basic Card -->
<div class="bg-white border border-neutral-200 rounded-xl p-6">
    Content
</div>

<!-- Interactive Card -->
<a href="..." class="block bg-white border border-neutral-200 rounded-xl p-6 hover:border-neutral-300 hover:shadow-sm transition-all">
    Content
</a>

<!-- No Border Card (for less emphasis) -->
<div class="bg-white rounded-xl p-6">
    Content
</div>
```

### Form Inputs
```html
<!-- Text Input -->
<input type="text" 
       class="w-full px-3 py-2.5 text-sm border border-neutral-200 rounded-lg focus:border-primary-500 focus:ring-2 focus:ring-primary-500/10 transition-colors"
       placeholder="Enter text...">

<!-- Textarea -->
<textarea 
    class="w-full px-3 py-2.5 text-sm border border-neutral-200 rounded-lg focus:border-primary-500 focus:ring-2 focus:ring-primary-500/10 transition-colors resize-none"
    rows="4"
    placeholder="Enter description..."></textarea>

<!-- Select -->
<select class="w-full px-3 py-2.5 text-sm border border-neutral-200 rounded-lg focus:border-primary-500 focus:ring-2 focus:ring-primary-500/10 transition-colors">
    <option>Option 1</option>
</select>

<!-- Label -->
<label class="block text-sm font-medium text-neutral-700 mb-2">
    Label Text
</label>

<!-- Helper Text -->
<p class="text-xs text-neutral-500 mt-1.5">
    Helper text goes here
</p>

<!-- Error Message -->
<p class="text-xs text-red-600 mt-1.5">
    Error message
</p>
```

### Badges
```html
<!-- Default Badge -->
<span class="inline-flex items-center gap-1 px-2.5 py-1 bg-neutral-100 text-neutral-700 text-xs font-medium rounded-md">
    Badge
</span>

<!-- Status Badges -->
<span class="inline-flex items-center gap-1 px-2.5 py-1 bg-green-100 text-green-700 text-xs font-medium rounded-md">
    Active
</span>

<span class="inline-flex items-center gap-1 px-2.5 py-1 bg-amber-100 text-amber-700 text-xs font-medium rounded-md">
    Warning
</span>

<span class="inline-flex items-center gap-1 px-2.5 py-1 bg-red-100 text-red-700 text-xs font-medium rounded-md">
    Urgent
</span>

<!-- With Icon -->
<span class="inline-flex items-center gap-1 px-2.5 py-1 bg-blue-100 text-blue-700 text-xs font-medium rounded-md">
    <svg class="w-3 h-3">...</svg>
    Badge
</span>
```

### Category Chips (Radio Buttons)
```html
<div class="flex flex-wrap gap-2">
    <label class="relative cursor-pointer">
        <input type="radio" name="category" value="all" class="peer sr-only">
        <span class="inline-flex items-center gap-1.5 px-3 py-2 text-sm font-medium text-neutral-700 bg-neutral-100 rounded-lg peer-checked:bg-primary-500 peer-checked:text-white transition-colors">
            All
        </span>
    </label>
    
    <label class="relative cursor-pointer">
        <input type="radio" name="category" value="roommate" class="peer sr-only">
        <span class="inline-flex items-center gap-1.5 px-3 py-2 text-sm font-medium text-neutral-700 bg-neutral-100 rounded-lg peer-checked:bg-primary-500 peer-checked:text-white transition-colors">
            🏠 Roommate
        </span>
    </label>
</div>
```

### Empty States
```html
<div class="flex flex-col items-center justify-center py-16 px-4">
    <!-- Icon -->
    <div class="w-16 h-16 mb-4 text-neutral-300">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="..."/>
        </svg>
    </div>
    
    <!-- Heading -->
    <h3 class="text-lg font-semibold text-neutral-900 mb-2">
        No posts found
    </h3>
    
    <!-- Description -->
    <p class="text-sm text-neutral-500 text-center max-w-sm mb-6">
        Try adjusting your filters or create your first post to get started.
    </p>
    
    <!-- Action -->
    <button class="inline-flex items-center gap-2 px-4 py-2.5 bg-primary-500 text-white text-sm font-medium rounded-lg hover:bg-primary-600 transition-colors">
        Create Post
    </button>
</div>
```

### Loading States
```html
<!-- Spinner -->
<div class="flex items-center justify-center py-12">
    <div class="w-8 h-8 border-2 border-neutral-200 border-t-primary-500 rounded-full animate-spin"></div>
</div>

<!-- Skeleton Card -->
<div class="bg-white border border-neutral-200 rounded-xl p-6 animate-pulse">
    <div class="h-4 bg-neutral-100 rounded w-3/4 mb-4"></div>
    <div class="h-4 bg-neutral-100 rounded w-1/2"></div>
</div>

<!-- Button Loading State -->
<button disabled class="inline-flex items-center gap-2 px-4 py-2.5 bg-primary-400 text-white text-sm font-medium rounded-lg cursor-not-allowed">
    <svg class="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24">
        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
    </svg>
    Processing...
</button>
```

### Dividers
```html
<!-- Horizontal -->
<div class="border-t border-neutral-200"></div>

<!-- With Text -->
<div class="relative my-6">
    <div class="absolute inset-0 flex items-center">
        <div class="w-full border-t border-neutral-200"></div>
    </div>
    <div class="relative flex justify-center">
        <span class="bg-white px-4 text-xs text-neutral-500">Or</span>
    </div>
</div>
```

## Page-Specific Patterns

### Home Page Hero
```html
<div class="bg-white border border-neutral-200 rounded-2xl p-8 md:p-12 mb-8">
    <h1 class="text-3xl md:text-4xl font-bold text-neutral-900 mb-3">
        Welcome to CampusHub
    </h1>
    <p class="text-lg text-neutral-600 mb-6">
        Your student community platform
    </p>
    <div class="flex flex-col sm:flex-row gap-3">
        <a href="..." class="inline-flex items-center justify-center gap-2 px-6 py-3 bg-primary-500 text-white text-sm font-medium rounded-lg hover:bg-primary-600 transition-colors">
            Get Started
        </a>
        <a href="..." class="inline-flex items-center justify-center gap-2 px-6 py-3 bg-neutral-100 text-neutral-700 text-sm font-medium rounded-lg hover:bg-neutral-200 transition-colors">
            Browse Posts
        </a>
    </div>
</div>
```

### Post Card (List View)
```html
<a href="..." class="block bg-white border border-neutral-200 rounded-xl overflow-hidden hover:border-neutral-300 hover:shadow-sm transition-all">
    <!-- Image -->
    <div class="aspect-video bg-neutral-100"></div>
    
    <!-- Content -->
    <div class="p-4">
        <!-- Badge -->
        <span class="inline-flex items-center gap-1 px-2.5 py-1 bg-blue-100 text-blue-700 text-xs font-medium rounded-md mb-3">
            Roommate
        </span>
        
        <!-- Title -->
        <h3 class="text-base font-semibold text-neutral-900 mb-2 line-clamp-2">
            Looking for roommate near campus
        </h3>
        
        <!-- Meta -->
        <div class="flex items-center gap-4 text-xs text-neutral-500 mb-3">
            <span class="flex items-center gap-1">
                <svg class="w-3.5 h-3.5">...</svg>
                Location
            </span>
            <span>2d ago</span>
        </div>
        
        <!-- Expiry Badge -->
        <span class="inline-flex items-center gap-1 px-2 py-1 bg-neutral-100 text-neutral-600 text-xs font-medium rounded">
                🕒 Expires in 15 days
        </span>
    </div>
</a>
```

### Filter Section
```html
<div class="bg-white border border-neutral-200 rounded-xl p-6 mb-6">
    <!-- Search -->
    <div class="mb-6">
        <label class="block text-sm font-medium text-neutral-700 mb-2">
            Search
        </label>
        <input type="text" 
               class="w-full px-3 py-2.5 text-sm border border-neutral-200 rounded-lg focus:border-primary-500 focus:ring-2 focus:ring-primary-500/10 transition-colors"
               placeholder="Search posts...">
    </div>
    
    <!-- Category Chips -->
    <div class="mb-6">
        <label class="block text-sm font-medium text-neutral-700 mb-3">
            Category
        </label>
        <div class="flex flex-wrap gap-2">
            <!-- Radio buttons styled as chips -->
        </div>
    </div>
    
    <!-- Buttons -->
    <div class="flex gap-2">
        <button type="submit" class="flex-1 px-4 py-2.5 bg-primary-500 text-white text-sm font-medium rounded-lg hover:bg-primary-600 transition-colors">
            Apply
        </button>
        <button type="reset" class="px-4 py-2.5 bg-neutral-100 text-neutral-700 text-sm font-medium rounded-lg hover:bg-neutral-200 transition-colors">
            Clear
        </button>
    </div>
</div>
```

## Implementation Status

### ✅ Completed
- Base template (base.html)
- CSS design system (style.css)
- Top navigation (mobile_nav.html)
- Bottom navigation (bottom_nav.html)
- Pagination component (pagination.html)
- Color system (8px spacing)
- Typography scale
- Component patterns documented

### 🔄 Remaining Templates to Update
Apply the same design patterns to:
1. Home page (core/home.html)
2. Post list (posts/post_list.html)
3. Post detail (posts/post_detail.html)
4. Post create/edit (posts/post_create.html, post_edit.html)
5. My posts (posts/my_posts.html)
6. Profile (accounts/profile.html)
7. Edit profile (accounts/edit_profile.html)
8. Login/Register (accounts/login.html, register.html)

## Key Principles

1. **Mobile-First**: All components responsive, touch-friendly
2. **8px Spacing**: Consistent rhythm, no arbitrary spacing
3. **Minimal**: Less visual noise, more white space
4. **Premium**: Subtle shadows, refined interactions
5. **Accessible**: Proper focus states, ARIA labels
6. **Fast**: Subtle transitions only (150ms)
7. **Consistent**: Same patterns everywhere

## Design Inspirations

- **Airbnb**: Clean cards, minimal borders, generous spacing
- **Notion**: Subtle hover states, clean typography
- **Linear**: Premium feel, refined interactions, minimal colors

---

*UI Polish completed by Senior Product Designer - July 23, 2026*
