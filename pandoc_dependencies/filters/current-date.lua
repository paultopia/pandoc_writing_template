-- directly taken from Pandoc docs at https://pandoc.org/lua-filters.html
function Meta(m)
  m.date = os.date("%B %e, %Y")
  return m
end
