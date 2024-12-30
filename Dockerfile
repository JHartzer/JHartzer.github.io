FROM jekyll/jekyll:4
COPY Gemfile ./
RUN bundle install