import math
def winsorize(values: list, lower_pct: float, upper_pct: float) -> list:
    """
    Returns values clipped to the interpolated percentile bounds.
    """
    # Write code here
    a=sorted(values)
    n=len(values)
   
    def get_perc(p):
        k=(n-1)*p/100.0
        i=int(k)
        j=math.ceil(k)
        return a[i]+(k-i)*(a[j]-a[i])
        
    lower_bound=get_perc(lower_pct)
    upper_bound=get_perc(upper_pct)
    return [max(lower_bound,min(upper_bound,x)) for x in values]