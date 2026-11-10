# QR Code - Accepts Payments

This Python script creates UPI payment QR codes from a UPI ID entered by the user.

## How It Works

1. The program asks for a UPI ID.
2. It builds a UPI payment link with payment details.
3. `qrcode.make()` turns the link into a QR-code image.
4. The images are saved as `google_pay_qr.png`, `phonepe_qr.png`, and `paytm_qr.png` and then opened for viewing.

The sample creates the same kind of UPI link for each filename; the QR codes are not app-specific.

## UPI Payment Link Details

A UPI link can look like this:

```text
upi://pay?pa=<UPI_ID>&pn=<NAME>&am=<AMOUNT>&tn=<NOTE>&cu=INR
```

- `pa` — Payee address: recipient's UPI ID.
- `pn` — Payee name: recipient's name.
- `am` — Amount to pay.
- `tn` — Transaction note, such as “Rent”.
- `cu` — Currency code, usually `INR`.
- `mc` — Merchant code. Use the real code for a merchant; omit it for a personal UPI account rather than using an invented value.
- `tid` — Transaction ID, when provided.
- `tr` — Transaction reference ID, when provided.
- `url` — Related URL, when needed.

Some details are optional and depend on the payment use case. Use accurate recipient and transaction information.

## Requirements

Install both required libraries from the terminal:

```bash
pip install qrcode pillow
```

- `qrcode` generates QR-code images.
- `Pillow` handles the images and supports displaying them.

## Run the Script

```bash
python qrcode.py
```

Enter a valid UPI ID when prompted. The generated images are saved in the current working directory.

## Important Note

The QR code stores payment details; it does not process a payment or contain the recipient's bank name. The payment app resolves the UPI ID and determines which recipient details to show. Check the recipient details in the payment app before approving a payment.
