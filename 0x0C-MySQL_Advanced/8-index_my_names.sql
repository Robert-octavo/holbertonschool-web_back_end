-- Create an index idx_name_first on the table names

-- and the fisrt letter of name

-- only the fisrt letter of the name must be indexed

CREATE INDEX idx_name_first ON names (name(1));