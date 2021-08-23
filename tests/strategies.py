from string import ascii_letters, digits

from dataset.csl import Variable
from hypothesis import assume
from hypothesis.strategies import composite, lists, sampled_from, text

alphanumerics = ascii_letters + digits + ".,()"

@composite
def flat_open_tags(draw) -> str:
    variable = draw(sampled_from(Variable))
    value = draw(text(alphanumerics, min_size=1))
    
    return f"<{variable.value}>{value}"

@composite
def nested_open_tags(draw) -> str:
    top_level_variable = draw(sampled_from(Variable))
    sub_level_variable = draw(sampled_from(Variable))

    assume(top_level_variable != sub_level_variable)
    value = draw(text(alphanumerics, min_size=1))
    
    return f"<{top_level_variable.value}><{sub_level_variable.value}>{value}"


@composite
def flat_close_tags(draw) -> str:
    variable = draw(sampled_from(Variable))
    value = draw(text(alphanumerics, min_size=1))
    
    return f"{value}</{variable.value}>"

@composite
def nested_close_tags(draw) -> str:
    top_level_variable = draw(sampled_from(Variable))
    sub_level_variable = draw(sampled_from(Variable))

    assume(top_level_variable != sub_level_variable)
    value = draw(text(alphanumerics, min_size=1))
    
    return f"{value}</{sub_level_variable.value}></{top_level_variable.value}>"

@composite
def flat_enclosed_tags(draw) -> str:
    variable = draw(sampled_from(Variable))
    value = draw(text(alphanumerics, min_size=1))
    
    return f"<{variable.value}>{value}</{variable.value}>"

@composite
def nested_enclosed_tags(draw) -> str:
    top_level_variable = draw(sampled_from(Variable))
    sub_level_variable = draw(sampled_from(Variable))
    
    assume(top_level_variable != sub_level_variable)
    value = draw(text(alphanumerics, min_size=1))
    
    return f"<{top_level_variable.value}><{sub_level_variable.value}>{value}</{sub_level_variable.value}></{top_level_variable.value}>"

@composite
def single_flat_tagged_sequence(draw) -> str:
    variable = draw(sampled_from(Variable))
    tokens = draw(lists(text(alphanumerics, min_size=1), min_size=2))

    return f"<{variable.value}>" + " ".join(tokens) + f"</{variable.value}>"

