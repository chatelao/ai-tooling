\version "2.24.0"

\include "paper_layout.ily"
\include "chords_header.ily"

\header {
  title = "Sinfonie Thema in c-Moll"
  composer = "Beispiel Komponist"
  tagline = ##f
}

melody = \relative c' {
  \clef treble
  \key c \minor
  \time 4/4

  c4 e8 g c4 g8 e |
  f4 a8 c f4 c8 a |
  g4 b8 d f4 d8 b |
  c1 \bar "|."
}

\score {
  <<
    \new ChordNames \harmonies
    \new Staff \melody
  >>
  \layout { }
  \midi {
    \tempo 4 = 120
  }
}
