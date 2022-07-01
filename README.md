# jekyll-bootstrap-theme

[![Gem Version](https://badge.fury.io/rb/jekyll-bootstrap-theme.svg)](https://badge.fury.io/rb/jekyll-bootstrap-theme)

A basic but extensible Jekyll theme based on Bootstrap 5.

[Theme preview](https://jonaharagon.github.io/jekyll-bootstrap-theme/) - **[One-Click Install (GitHub Pages)](https://github.com/jonaharagon/jekyll-bootstrap-template/generate)** - [RubyGems.org](https://rubygems.org/gems/jekyll-bootstrap-theme)

![Bootstrap theme preview](/screenshot.png)

## Install

If you are able to install custom Gems on your build server/web server, install via the **Gemfile** method described here. GitHub Pages users cannot install custom Gems, and must instead use the **Remote Theme** Jekyll plugin to use this theme.

### Gemfile

Add this line to your `Gemfile`:

```ruby
gem 'jekyll-bootstrap-theme'
```

And add this line to your site's `_config.yml`:

```yaml
theme: jekyll-bootstrap-theme
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install jekyll-bootstrap-theme

### Remote Theme (GitHub Pages)

#### One-Click Install

- **[Create Repository from Pre-Made Template](https://github.com/jonaharagon/jekyll-bootstrap-template/generate)**

#### Manual Install

GitHub Pages websites cannot use custom Gems. Instead, you can add this repository as a `remote_theme`:

After making a Jekyll repo, add `gem "jekyll-remote-theme"` to the `:jekyll_plugins` group in your `Gemfile`, then run `bundle` to install the plugin:

```ruby
group :jekyll_plugins do
  [...]
  gem "jekyll-remote-theme"
end
```

Add the following to your site's `_config.yml` to activate the plugin and select this theme:

```yaml
plugins:
  - jekyll-remote-theme

remote_theme: jonaharagon/jekyll-bootstrap-theme
```

Optionally, you can specify a [release](https://github.com/jonaharagon/jekyll-bootstrap-theme/releases), [branch](https://github.com/jonaharagon/jekyll-bootstrap-theme/branches), or [tag](https://github.com/jonaharagon/jekyll-bootstrap-theme/tags) to lock the theme version in place:

```yaml
remote_theme: jonaharagon/jekyll-bootstrap-theme@v0.1.0
```

## Theme Contents

### Layouts

Files within the `_layouts` directory, that define the markup for your theme:

 - `default.html` - The base layout that lays the foundation for subsequent layouts. Includes a navigation bar and footer on all pages.
 - `home.html` - The layout for your homepage/landing page. Includes a blog post listing with pagination support.
 - `page.html` - The layout for documents and other pages that contain Front Matter, that are not posts.
 - `post.html` - The layout for your blog posts.

#### Home Layout

##### Main Heading, Custom Content Injection

The home layout will inject all content from your `index.md` / `index.html` before the optional posts heading. This will allow you to include non-posts related content to be published on the landing page under a dedicated heading. We recommended that you title this section with a Heading2 (##), and enable a posts heading if you add additional content.

##### Posts Listing

It will be automatically included only when your site contains one or more valid posts or drafts (if the site is configured to show_drafts).

This section is untitled by default. You can customize this heading by defining a `list_title` variable in the document's front matter, which will be rendered with an `<h2>` tag.

### Includes

Snippets of code within the _includes directory that can be inserted in multiple layouts (and another include-file as well) within the same theme-gem:

 - `footer.html` — Defines the site's footer section.
 - `head.html` — Code-block that defines the `<head></head>` in default layout.
 - `custom-head.html` — Placeholder to allow users to add more metadata to `<head />`.
 - `header.html` — Defines the site's main header section. By default, pages with a defined `title` attribute will have links displayed here.
 - `social.html` — Renders social-media icons based on the `bootstrap.social_links` data in the config file.

### Sass

`.scss` files within the `_sass` directory that define the theme's styles.

 - `bootstrap/*` - Default Bootstrap SCSS files.
 - `_custom-variables.scss` - This file can be overridden to add any custom variables. It is loaded *after* Bootstrap's variables but *before* the rest of Bootstrap, allowing you to override any of [Bootstrap's variables](https://github.com/twbs/bootstrap/blob/main/scss/_variables.scss). (*Note: Cannot override styles*)
 - `_custom-styles.scss` - This file can be overridden to add any custom styles. It is loaded *after* all other CSS. (*Note: Cannot override variables*)

### Assets

 - `assets/css/bootstrap-theme.scss` - Imports sass files from `_sass` and gets processed into the final stylesheet.
 - `assets/css/bootstrap-icons.css` - Loads [Bootstrap Icons](https://icons.getbootstrap.com)
 - `assets/js/bootstrap.bundle.min.js` - Bootstrap's Javascript bundle, loaded on every page by default.
 - `assets/fonts/bootstrap-icons.woff(2)` - Bootstrap Icons font files.

### Plugins

This theme comes with [`jekyll-seo-plugin`](https://github.com/jekyll/jekyll-seo-tag) preinstalled to make sure your website gets the most useful meta tags. See [usage](https://github.com/jekyll/jekyll-seo-tag#usage) to know how to set it up.

## Configuration

This theme can be configured with various settings in [`_config.yml`](/_config.yml).

### Site Author

`site.author` is expected to be a mapping of attributes instead of a simple scalar value:

```yaml
author:
  name: 'Github User'
  email: 'github@example.com'
```

### Navbar Customization

If you want to link only specific pages in your header, uncomment this and add the path to the pages in order as they should show up

```yaml
bootstrap:
  header_pages:
   - about.md
   - second.html
   - folder/third.md
```

### Social Network Icons

You can add links to the accounts you have on other sites, with respective icon, by adding one or more of the following options in your config. These must be complete URLs to function properly.

```yaml
bootstrap:
  social_links:
    twitter: 'https://example.com/@jekyllrb'
    github:  'https://example.com/@jekyllrb'
    facebook: 'https://example.com/@jekyllrb'
    instagram: 'https://example.com/@jekyllrb'
    linkedin: 'https://example.com/@jekyllrb'
    google: 'https://example.com/@jekyllrb'
    youtube: 'https://example.com/@jekyllrb'
    twitch: 'https://example.com/@jekyllrb'
    telegram: 'https://example.com/@jekyllrb'
    whatsapp: 'https://example.com/@jekyllrb'
    discord: 'https://example.com/@jekyllrb'
    slack: 'https://example.com/@jekyllrb'
```

### Post Excerpts

To display post excerpts on the Home layout, set `site.excerpts.show` to true. You can also choose to automatically cut off excerpts after 32 words (approx. 2 lines):

```yaml
excerpts:
  show: true
  auto_truncate: true
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/jonaharagon/jekyll-bootstrap-theme. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

**Development Requirements:**

- `yarn`

Updating packages: `yarn run assets:clean && yarn upgrade && yarn run assets:install`

## License

The theme is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
