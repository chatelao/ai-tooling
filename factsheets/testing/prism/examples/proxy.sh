#!/bin/bash
# Prism als Proxy zu einem existierenden Server nutzen, um Anfragen/Antworten zu validieren
npx prism proxy api.yaml http://localhost:8080 --errors
