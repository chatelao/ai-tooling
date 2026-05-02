import os
import yaml

def generate_mkdocs_config():
    config = {
        'site_name': 'KI-Agenten Werkzeuge & Quellen',
        'repo_url': 'https://github.com/chatelao/ai-tooling',
        'docs_dir': 'docs',
        'theme': {
            'name': 'material',
            'features': [
                'navigation.tabs',
                'navigation.sections',
                'navigation.expand',
                'navigation.top',
                'search.suggest',
                'search.highlight',
                'content.code.copy'
            ],
            'language': 'de',
            'palette': [
                {
                    'media': '(prefers-color-scheme: light)',
                    'scheme': 'default',
                    'primary': 'indigo',
                    'accent': 'indigo',
                    'toggle': {
                        'icon': 'material/brightness-7',
                        'name': 'Switch to dark mode'
                    }
                },
                {
                    'media': '(prefers-color-scheme: dark)',
                    'scheme': 'slate',
                    'primary': 'indigo',
                    'accent': 'indigo',
                    'toggle': {
                        'icon': 'material/brightness-4',
                        'name': 'Switch to light mode'
                    }
                }
            ]
        },
        'plugins': [
            'search',
            {
                'with-pdf': {
                    'author': 'KI-Agenten Team',
                    'copyright': '2024 KI-Agenten Team',
                    'output_path': 'ki-agenten-werkzeuge.pdf',
                    'cover': True,
                    'toc_title': 'Inhaltsverzeichnis'
                }
            }
        ],
        'markdown_extensions': [
            'admonition',
            'attr_list',
            'def_list',
            'footnotes',
            'md_in_html',
            'toc',
            {
                'pymdownx.highlight': {
                    'anchor_linenums': True,
                    'line_spans': '__span',
                    'pygments_lang_class': True
                }
            },
            'pymdownx.inlinehilite',
            'pymdownx.snippets',
            'pymdownx.superfences',
            {
                'pymdownx.tabbed': {
                    'alternate_style': True
                }
            },
            'tables'
        ],
        'nav': []
    }

    # Main navigation
    config['nav'].append({'Home': 'README.md'})
    config['nav'].append({'Strategie': 'GEMINI.md'})
    config['nav'].append({'Werkzeuge': 'TOOLS.md'})
    config['nav'].append({'Datenquellen': 'DATASOURCES.md'})
    config['nav'].append({'Visualisierung': 'VISUALIZATION.md'})
    config['nav'].append({'Roadmap': 'FACTSHEET_ROADMAP.md'})

    # Factsheets navigation
    factsheets_nav = [{'Übersicht': 'factsheets/README.md'}]

    real_factsheets_dir = 'factsheets'
    groups = sorted([d for d in os.listdir(real_factsheets_dir) if os.path.isdir(os.path.join(real_factsheets_dir, d))])

    for group in groups:
        group_path = os.path.join(real_factsheets_dir, group)
        group_readme = os.path.join(group_path, 'README.md')

        group_items = []
        if os.path.exists(group_readme):
            group_items.append({'Übersicht': f'factsheets/{group}/README.md'})

        tools = sorted([d for d in os.listdir(group_path) if os.path.isdir(os.path.join(group_path, d))])
        for tool in tools:
            tool_path = os.path.join(group_path, tool)

            tool_items = []

            # Recursively find all Markdown files
            for root, dirs, files in os.walk(tool_path):
                # Skip examples directory for navigation to keep it clean
                if 'examples' in root.split(os.sep):
                    continue

                for file in sorted(files):
                    if file.endswith('.md'):
                        rel_path = os.path.relpath(os.path.join(root, file), real_factsheets_dir)
                        # Create a nice name
                        if file == 'README.md':
                            if root == tool_path:
                                name = 'Zusammenfassung'
                            else:
                                sub_dir = os.path.basename(root)
                                name = f'Übersicht {sub_dir.title()}'
                        else:
                            name = os.path.splitext(file)[0].replace('-', ' ').replace('_', ' ').title()

                        tool_items.append({name: f'factsheets/{rel_path}'})

            display_name = tool.replace('-', ' ').title()
            if len(tool_items) > 1:
                # Ensure Summary is first
                tool_items.sort(key=lambda x: 0 if 'Zusammenfassung' in x else 1)
                group_items.append({display_name: tool_items})
            elif len(tool_items) == 1:
                group_items.append({display_name: list(tool_items[0].values())[0]})

        if group_items:
            factsheets_nav.append({group.capitalize(): group_items})

    config['nav'].append({'Factsheets': factsheets_nav})

    # Exclude non-documentation files from the build
    exclude_list = [
        '**/*.sh',
        '**/*.hash.sha256',
        '**/*.log',
        '**/node_modules/**',
        'log/**',
        'site/**',
        '**/examples/**', # Exclude all examples
    ]
    config['exclude_docs'] = "\n".join(exclude_list)

    with open('mkdocs.yml', 'w', encoding='utf-8') as f:
        yaml.dump(config, f, allow_unicode=True, sort_keys=False)

if __name__ == "__main__":
    generate_mkdocs_config()
