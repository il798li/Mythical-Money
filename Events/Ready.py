import Main, Refresh
async def on_ready():
    await Refresh.refresh(
        Main.mm
    )
def setup(
    mm
):
    mm.add_listener(
        on_ready
    )