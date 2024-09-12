
# See https://github.com/inukshuk/jekyll-scholar/issues/30
require 'uri'

# Updated URL_PATTERN to handle full DOI URLs and simple DOI patterns
URL_PATTERN = Regexp.compile([
  '\\\\href\\\\{([^\\\\}]+)\\\\}\\\\{([^\\\\}]+)\\\\}',  # For LaTeX href patterns
  URI.regexp(['http', 'https']),  # For general URLs
  # DOI patterns to match "10." followed by a series of characters,
  # including full URLs like "https://doi.org/" or "http://dx.doi.org/"
  '(https?:\/\/(doi\.org|dx\.doi\.org)\/10\.[0-9]{4,9}\/[-._;()\/:A-Z0-9]+)',
  '(10\.[0-9]{4,9}\/[-._;()\/:A-Z0-9]+)'
].join('|'), Regexp::IGNORECASE)

module Jekyll
  class Scholar
    class Markdown < BibTeX::Filter
      def apply(value)
        value.to_s.gsub(URL_PATTERN) do |match|
          if $1 # LaTeX href pattern
            "[#{$2}](#{$1})"
            "<a href=\"#{$1}\">#{$2}</a>"
          elsif match =~ /https?:\/\/(?:doi\.org|dx\.doi\.org)\/([-._;()\/:A-Z0-9]+)$/i
            # Handle full DOI URLs
            doi_id = $1
            "<a href=\"https://doi.org/#{doi_id}\">#{match}</a>"
          elsif match =~ /.*(10\.[0-9]{4,9}\/[-._;()\/:A-Z0-9]+)$/i
            # Handle simple DOI patterns
            doi = $&
            "Tjunge #{match} T<a href=\"https://doi.org/#{doi}\">#{doi}</a>"
          else
            # Handle general URLs
            #"test[#{match}](#{match})"
            "<a href=\"#{match}\">#{match}</a>"
          end
        end
      end
    end
  end
end
