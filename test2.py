def ans_box(config):
    if not config or not isinstance(config, list):
        return
    
    # Extract content from config
    content = [line['text'] for line in config]
    
    # Calculate maximum content width
    content_width = max(len(line) for line in content)
    
    # Create dynamic borders
    horizontal_border = "─" * (content_width + 2)
    top_border = f"┌{horizontal_border}┐"
    bottom_border = f"└{horizontal_border}┘"
    divider = f"├{horizontal_border}┤"
    
    # Print the box
    print(top_border)
    for i, line in enumerate(config):
        text = line['text']
        align = line.get('align', 'left')
        
        # Handle alignment
        if align == 'center':
            padding_left = (content_width - len(text)) // 2
            padding_right = content_width - len(text) - padding_left
        elif align == 'right':
            padding_left = content_width - len(text)
            padding_right = 0
        else:
            padding_left = 0
            padding_right = content_width - len(text)
        
        # Print the line with padding
        print(f"│ {' ' * padding_left}{text}{' ' * padding_right} │")
        
        # Handle dividers based on config
        if line.get('divider', False):
            print(divider)
    print(bottom_border)

# Example usage:
bisection_ans, bisection_iterations = 1.23, 5
position_ans, position_iterations = 1.22, 6
difference = 100 - (abs(bisection_ans - position_ans) / bisection_ans * 100)

config = [
    {'text': 'Roots Calculated:', 'align': 'center', 'divider': True},
    {'text': f"Bisection  Method     │ {bisection_ans} after {bisection_iterations} iterations"},
    {'text': f"False Position Method │ {position_ans} after {position_iterations} iterations", 'divider': True},
    {'text': f"Accuracy │ {difference:.2f}%", 'align': 'right'}
]

ans_box(config)
