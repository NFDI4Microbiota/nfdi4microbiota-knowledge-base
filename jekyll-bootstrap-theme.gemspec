# frozen_string_literal: true

version = "1.1.0"

Gem::Specification.new do |spec|
  spec.name          = "jekyll-bootstrap-theme"
  spec.version       = version
  spec.homepage      = "https://github.com/jonaharagon/jekyll-bootstrap-theme"

  spec.author        = "Jonah Aragon"
  spec.email         = "jonah@triplebit.net"
  spec.cert_chain    = ['certs/jonaharagon.pem']
  spec.signing_key   = File.expand_path("~/.ssh/gem-private_key.pem") if $0 =~ /gem\z/

  spec.metadata = {
    "bug_tracker_uri"   => "https://github.com/jonaharagon/jekyll-bootstrap-theme/issues",
    "changelog_uri"     => "https://github.com/jonaharagon/jekyll-bootstrap-theme/releases/tag/v#{version}",
    "documentation_uri" => "https://www.rubydoc.info/gems/jekyll-bootstrap-theme/#{version}",
    "homepage_uri"      => "https://jonaharagon.github.io/jekyll-bootstrap-theme",
    "source_code_uri"   => "https://github.com/jonaharagon/jekyll-bootstrap-theme/tree/v#{version}",
    "funding_uri"       => "https://github.com/sponsors/jonaharagon",
    "plugin_type"       => "theme"
  }

  spec.summary       = "A Bootstrap 5 theme for Jekyll."
  spec.license       = "MIT"
  spec.description = <<-EOF
    A basic but extensible Jekyll theme based on Bootstrap 5,
    with support for GitHub Pages and Bootstrap Icons.
  EOF

  spec.required_ruby_version = '>= 2.4.0'
  spec.required_rubygems_version = '>= 2.7.0'

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_layouts|_includes|_sass|LICENSE|README)!i) }

  spec.add_runtime_dependency "jekyll", ">= 4.0", "<5.0"
  spec.add_runtime_dependency "jekyll-feed", "~> 0.9"
  spec.add_runtime_dependency "jekyll-seo-tag", "~> 2.1"

  spec.add_development_dependency "webrick", "~> 1.7"
  spec.add_development_dependency "bundler", "~> 2.2"
end
