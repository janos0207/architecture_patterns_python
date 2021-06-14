from model import OrderLine


def test_orderline_mapper_can_load_lines(session):
    session.execute(
        'INSERT INTO order_lines (orderid, sku, qty) VALUES'
        '("order1", "RED-CHAIR", 12),'
        '("order1", "RED-TABLE", 13),'
        '("order1", "BLUE-LIPSTICK", 14)'
    )

    expected = [
        OrderLine("order1", "RED-CHAIR", 12),
        OrderLine("order1", "RED-TABLE", 13),
        OrderLine("order1", "BLUE-LIPSTICK", 14),
    ]

    assert session.query(OrderLine).all() == expected
