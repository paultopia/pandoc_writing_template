-- fix-possessives.lua

-- totally vibe-coded with gemini seeing as I don't know either lua or pandoc's lua API, may have bugs

-- Function to target and fix strings containing the capitalized possessive
local function fix_possessive_str(el)
  -- Quick check to see if the string contains the sequence before doing regex
  if el.text:find("'S") or el.text:find("’S") then
    -- [%w\128-\255] matches any ASCII alphanumeric OR any UTF-8 byte.
    -- This ensures we catch normal words (Author'S) and accented words (José'S),
    -- but ignores 'S at the very beginning of a string (like a quote).
    el.text = el.text:gsub("([%w\128-\255])'S", "%1's")
    
    -- Do the exact same thing for typographic (curly) apostrophes
    el.text = el.text:gsub("([%w\128-\255])’S", "%1’s")
  end
  return el
end

-- Helper function to traverse the contents of specific AST elements
local function process_blocks(blocks)
  -- Wrap blocks in a temporary Div so we can use pandoc.walk_block on them
  local temp_div = pandoc.Div(blocks)
  temp_div = pandoc.walk_block(temp_div, {
    Str = fix_possessive_str
  })
  return temp_div.content
end

-- The main filter targets only Footnotes (Note) and the References list (Div with id="refs")
return {
  {
    Note = function(el)
      el.content = process_blocks(el.content)
      return el
    end,
    Div = function(el)
      if el.identifier == "refs" then
        el.content = process_blocks(el.content)
        return el
      end
    end
  }
}
