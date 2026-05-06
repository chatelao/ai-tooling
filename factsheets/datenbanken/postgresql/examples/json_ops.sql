-- Create a table with a JSONB column
CREATE TABLE ai_models (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    metadata JSONB
);

-- Insert data with JSON
INSERT INTO ai_models (name, metadata) VALUES
('Llama-3', '{"parameters": "70B", "type": "LLM", "tags": ["meta", "open-source"]}'),
('GPT-4', '{"parameters": "unknown", "type": "LLM", "tags": ["openai", "proprietary"]}');

-- Query JSONB properties
SELECT name, metadata->>'parameters' as params
FROM ai_models
WHERE metadata @> '{"type": "LLM"}';

-- Search in JSONB array
SELECT name
FROM ai_models
WHERE metadata->'tags' ? 'open-source';
