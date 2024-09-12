
# Contributed by @mfenner
# See https://github.com/inukshuk/jekyll-scholar/issues/30
require 'uri'

URL_PATTERN = Regexp.compile([
  '\\\\href\\\\{([^\\\\}]+)\\\\}\\\\{([^\\\\}]+)\\\\}',
  URI.regexp(['http', 'https', 'ftp']),
  # DOI patterns to match "10." followed by a series of characters, including full URLs
  '(https?://doi\.org/[-._;()/:A-Z0-9]+|http://dx\.doi\.org/[-._;()/:A-Z0-9]+|10\.[0-9]{4,9}/[-._;()/:A-Z0-9]+)', # This regex matches DOIs in different forms
].join('|'), Regexp::IGNORECASE)

module Jekyll
  class Scholar
    class Markdown < BibTeX::Filter
      def apply(value)
        value.to_s.gsub(URL_PATTERN) do |match|
          if $1 # If we have a URL pattern match
            "[#{$2}](#{$1})"
            "<a href=\"#{$1}\">#{$2}</a>"
          elsif $& =~ /^https?:\/\/(doi\.org|dx\.doi\.org)\/([-._;()/:A-Z0-9]+)$/i # If we have a DOI URL match
            doi = $&
            doi_id = $2
            "<a href=\"https://doi.org/#{doi_id}\">#{doi}</a>"
          elsif $& =~ /^(10\.[0-9]{4,9}\/[-._;()/:A-Z0-9]+)$/i # If we have a DOI match without URL
            doi = $&
            "<a href=\"https://doi.org/#{doi}\">#{doi}</a>"
          else
            "[#{$&}](#{$&})"
            "<a href=\"#{$&}\">#{$&}</a>"
          end
        end
      end
    end
  end
end
