import numpy as np

def generate_report(gray, brighter, blurred_gray, white_pct):
    counts, bin_edges = np.histogram(gray.flatten(), bins=8, range=(0, 256))

    overexposed_px = (gray >= 250).sum()
    overexposed_pct = (overexposed_px / gray.size) * 100

    underexposed_px = (gray <= 5).sum()
    underexposed_pct = (underexposed_px / gray.size) * 100

    line = "═══════════════════════════════════════════════════════════"

    report = f"""{line}

   PIXELWORKS AI — IMAGE REPORT

{line}

IMAGE PROPERTIES
  Dimensions  : {gray.shape[0]} × {gray.shape[1]} pixels
  Channels    : 1 (Grayscale)
  Total Pixels: {gray.size:,}
  Data Type   : {gray.dtype}

BRIGHTNESS STATS
  Min : {gray.min()}        Max : {gray.max()}
  Mean: {gray.mean():.1f}    Std : {gray.std():.1f}

EXPOSURE ANALYSIS
  Overexposed  (≥250): {overexposed_px:<5} pixels ({overexposed_pct:.2f}%)
  Underexposed (≤5)  : {underexposed_px:<5} pixels ({underexposed_pct:.2f}%)

PIXEL DISTRIBUTION (8 bins)"""

    for i in range(8):
        bin_range = f"{int(bin_edges[i])}-{int(bin_edges[i+1])-1}"
        bar = "█" * int(counts[i] / 1000)
        report += f"\n  {bin_range:<6} : {bar} {counts[i]} px"

    report += f"""

FILTERS APPLIED
  ☑ Brightness +50  | New mean: {brighter.mean():.1f}
  ☑ Box Blur        | Std dev:  {blurred_gray.std():.1f}
  ☑ Threshold 128   | White %:  {white_pct:.1f}%

{line}"""

    return report