import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_invitations(template, attendees):
    # Validate template type
    if not isinstance(template, str):
        logging.error("Invalid input type: template must be a string.")
        return

    # Validate attendees type
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        logging.error("Invalid input type: attendees must be a list of dictionaries.")
        return

    # Check if template is empty
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        # Safely get values with fallback to 'N/A'
        name = attendee.get('name', 'N/A')
        event_title = attendee.get('event_title', 'N/A')
        event_date = attendee.get('event_date', 'N/A')
        event_location = attendee.get('event_location', 'N/A')

        # Replace placeholders in the template
        filled_template = template.replace("{name}", name)
        filled_template = filled_template.replace("{event_title}", event_title)
        filled_template = filled_template.replace("{event_date}", event_date)
        filled_template = filled_template.replace("{event_location}", event_location)

        # Write to output file
        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, 'w') as f:
                f.write(filled_template)
            logging.info(f"Generated file: {output_filename}")
        except Exception as e:
            logging.error(f"Failed to write file {output_filename}: {e}")

# Example usage:
template_text = (
    "Hello {name},\n\n"
    "You're invited to the {event_title}!\n"
    "Date: {event_date}\n"
    "Location: {event_location}\n"
)

attendees_list = [
    {"name": "Alice", "event_title": "Spring Gala", "event_date": "May 10", "event_location": "Town Hall"},
    {"name": "Bob", "event_title": "Spring Gala", "event_date": "May 10"},  # Missing location
    {"name": "Charlie", "event_location": "City Park"}  # Missing title and date
]

# Call the function
generate_invitations(template_text, attendees_list)
