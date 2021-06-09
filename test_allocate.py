from datetime import date, timedelta
from model import allocate, Batch, OrderLine

now = date.today()
tomorrow = now + timedelta(days=1)

def test_prefers_current_stock_batches_to_shipments():
    in_stock_batch = Batch('in-stock-batch', 'RETRO-CLOCK', 100, eta=None)
    shipment_batch = Batch('shipment-batch', 'RETRO-CLOCk', 100, eta=tomorrow)
    line = OrderLine('oref', 'RETRO-CLOCK', 10)

    allocate(line, [in_stock_batch, shipment_batch])

    assert in_stock_batch.available_quantity == 90
    assert shipment_batch.available_quantity == 100
