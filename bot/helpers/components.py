from hikari.impl.special_endpoints import ActionRowBuilder
from hikari import ButtonStyle
def ticket_close_button(button_label: str = "Close", button_emoji: chr = None, button_id: str = "ticket_close", button_style: ButtonStyle = ButtonStyle.SECONDARY):
    row = ActionRowBuilder()
    button = row.add_button(button_style, button_id)
    button.set_label(button_label)
    if button_emoji:
        button.set_emoji(button_emoji)
    button.add_to_container()
    return row

def confirmation_menu(
                      cancel_label: str = "Cancel",
                      cancel_emoji: chr = None,
                      cancel_id: str = "ticket_confirmation_false",
                      cancel_style: ButtonStyle = ButtonStyle.SECONDARY,
                      close_label: str = "Close",
                      close_emoji: chr = None,
                      close_id: str = "ticket_confirmation_true",
                      close_style: ButtonStyle = ButtonStyle.DANGER):
    row = ActionRowBuilder()
    # Cancel button
    cancel = row.add_button(cancel_style, cancel_id)
    cancel.set_label(cancel_label)
    if cancel_emoji:
        cancel.set_emoji(cancel_emoji)
    cancel.add_to_container()
    # Close button
    close = row.add_button(close_style, close_id)
    close.set_label(close_label)
    if close_emoji:
        close.set_emoji(close_emoji)
    close.add_to_container()
    return row
