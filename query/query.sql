SELECT order_id,
           order_date,
           a.user_id,
           b.payment_name,
           c.shipper_name,
           order_price,
           order_discount,
           d.voucher_name,
           d.voucher_price,
           order_total,
           e.rating_status
FROM andrewsu_data_raw.tb_orders a
        LEFT JOIN andrewsu_data_raw.tb_payments b on a.payment_id = b.payment_id
        LEFT JOIN andrewsu_data_raw.tb_shippers c on a.shipper_id = c.shipper_id
        LEFT JOIN andrewsu_data_raw.tb_vouchers d on a.voucher_id = d.voucher_id
        LEFT JOIN andrewsu_data_raw.tb_ratings e on a.rating_id = e.rating_id;