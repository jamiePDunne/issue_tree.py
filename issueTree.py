import graphviz as gv

# Create the issue tree data
data = {
    'Executive Overview': [
        'Business Development',
        'Product Management',
        'Technology',
        'Operations',
        'Compliance',
        'Marketing',
        'Customer Support'
    ],
    'Business Development': [
        'Partnerships',
        'Client Acquisition',
        'Revenue Streams'
    ],
    'Product Management': [
        'Platform Features',
        'User Experience',
        'Roadmap Planning'
    ],
    'Technology': [
        'Architecture Design',
        'Software Development',
        'API Integration',
        'Security Measures',
        'QA and Testing'
    ],
    'Operations': [
        'Trade Execution',
        'Account Management',
        'Transaction Processing',
        'Infrastructure Management'
    ],
    'Compliance': [
        'Regulatory Compliance',
        'KYC/AML Procedures',
        'Risk Monitoring'
    ],
    'Marketing': [
        'Brand Awareness',
        'User Acquisition',
        'Advertising Campaigns',
        'Community Building'
    ],
    'Customer Support': [
        'Helpdesk Services',
        'Query Resolution',
        'User Education'
    ]
}

# Define color codes for nodes
color_codes = {
    'Technology': 'lightblue',
    'QA and Testing': 'lightgreen'
}

# Create the Graphviz graph
graph = gv.Digraph(format='png')
graph.attr('node', shape='box')
graph.attr(rankdir='LR', ranksep='0.5')  # Change layout to left to right (LR) and set rank separation

def add_nodes_edges(data, parent_node):
    child_nodes = data.get(parent_node, [])

    for node in child_nodes:
        if node in color_codes:
            graph.node(node, style='filled', fillcolor=color_codes[node])
        else:
            graph.node(node)
        graph.edge(parent_node, node)
        add_nodes_edges(data, node)

# Add nodes and edges to the graph
add_nodes_edges(data, 'Executive Overview')

# Render and save the graph
graph.render('Executive_Overview_digital_asset_platform_issue_tree', view=True)
