# You own a weather station.
# You have predictions for several upcoming days of rainfall and evaporation.
# You can put the bucket out at midnight on any day.
# You can collect it later in the week at midnight.
# Determine how to maximize the amount of rain collected.

# Example:
# [(10r, 5e), (2r, 4e), (6r, 5e), (9r, 2e), (3r, 1e), (2r, 8e), (4r, 4e)]

def maximum_rain(forecast):
    """
    Given a forecast, which is a list of (rainfall, evaporation) tuples, like:
    [(10, 5), (2, 4), (6, 5), (9, 2), (3, 1), (2, 8), (4, 4)]
    returns a starting index and ending index of when bucket should be
    put outside and brought inside.
    """
    if not forecast:
        return (None, None)

    # Combine precipitations and evaporations into a single number per day.
    combined_forecast = [day[0] - day[1] for day in forecast]

    # Combine successive positive and negative numbers into a single value,
    # keeping track of the original starting indices of each value.
    negative_run = combined_forecast[0] <= 0
    orig_idxs = [0]
    condensed = []
    accumulated = 0
    for idx, f in enumerate(combined_forecast):
        if (negative_run and f <= 0) or (not negative_run and f > 0):
            # Accumulate this value.
            accumulated += f
        else:
            # Add the accumulated value.
            condensed.append(accumulated)
            # Add this original index.
            orig_idxs.append(idx)
            # Restart the accumulator with the new value.
            accumulated = f
            # Flip the state between accumulating negative/positive values.
            negative_run = not negative_run

    # Accumulate the final value.
    condensed.append(accumulated)

    if len(condensed) == 0:
        return (None, None)

    curr_idx = 0
    # If the first value is not positive, skip past it.
    # So start the traversal at the first positive value.
    if condensed[0] <= 0:
        curr_idx = 1

    start_idx = finish_idx = None

    while curr_idx < len(orig_idxs):

        if start_idx == None:
            # Set initial values of start/finish index.
            start_idx = finish_idx = orig_idxs[curr_idx]

        # Is this the last condensed value?
        if curr_idx == len(orig_idxs) - 1:
            # Last value.
            if condensed[curr_idx] > 0:
                # Positive so include it.
                finish_idx = len(combined_forecast) - 1
            else:
                # Negative so don't include it - use the last index instead.
                finish_idx = max(0, orig_idxs[curr_idx] - 1)
            break

        if condensed[curr_idx] > 0:
            # Only the initial value will be positive.
            # Start here, then begin considering (negative, positive) pairs for addition.
            start_idx = orig_idxs[curr_idx]
            curr_idx += 1
        elif condensed[curr_idx] + condensed[curr_idx + 1] > 0:
            # Only take negative values if the value plus the next positive
            # value is greater than zero.
            finish_idx = orig_idxs[curr_idx]
            curr_idx += 2
        else:
            # (negative, positive) pair is not a net postive, so end here.
            finish_idx = orig_idxs[curr_idx] - 1
            break

    # Return as 1-based days in the forecast list.
    if start_idx is not None:
        start_idx += 1
    if finish_idx is not None:
        finish_idx += 1

    return (start_idx, finish_idx)
