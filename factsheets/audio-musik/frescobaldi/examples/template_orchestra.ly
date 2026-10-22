\version "2.24.0"

\header {
  title = "Orchestral Overture"
  composer = "Frescobaldi Template"
  tagline = "Created with Frescobaldi & LilyPond"
}

global = {
  \key c \major
  \time 4/4
  \tempo "Allegro maestoso" 4 = 120
}

flute = \relative c'' {
  \global
  c4 e g c |
  b4. a8 g2 |
  f4 a d c |
  b1 \bar "|."
}

violin = \relative c' {
  \global
  c8 e g e c e g e |
  d8 g b g d g b g |
  c,8 f a f c f a f |
  g8 b d b g2 \bar "|."
}

cello = \relative c {
  \global
  \clef bass
  c2 e |
  g2 b, |
  a2 f |
  g1 \bar "|."
}

\score {
  <<
    \new StaffGroup <<
      \new Staff \with { instrumentName = "Flute" } \flute
      \new Staff \with { instrumentName = "Violin I" } \violin
      \new Staff \with { instrumentName = "Cello" } \cello
    >>
  >>
  \layout { }
  \midi { }
}
