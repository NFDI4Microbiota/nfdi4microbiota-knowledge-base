require 'jekyll/scholar'
require 'uri'

module MarkdownFilter
  class Markdown < BibTeX::Filter
    def apply(value)
      url = value.to_s.slice(URI.regexp(['http','https','ftp']))
      value = url ? "[#{url}](#{url})" : value
    end
  end
end