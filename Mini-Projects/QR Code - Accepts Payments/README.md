# QR Code - Accepts Payments

This Python script creates UPI payment QR codes for Google Pay, PhonePe, and Paytm from a UPI ID entered by the user.

## How It Works

1. Prompts for a UPI ID and stores the input in `upi_id`.
2. Builds a UPI payment URI for each app, for example:
   `upi://pay?pa=<UPI_ID>&pn=<RECIPIENT_NAME>&mc=<MERCHANT_CODE>`
3. Uses the `qrcode` library to turn each URI into a QR-code image.
4. Saves the images as `google_pay_qr.png`, `phonepe_qr.png`, and `paytm_qr.png`.
5. Calls `.show()` to open each generated image in the system's default image viewer.

The `pa` parameter is the payee's UPI ID, `pn` is the payee name, and `mc` is the merchant code. The supplied script uses the same URI format for all three apps; these are not app-specific payment links.

## Requirements

Install the QR-code library before running the script:

```bash
python -m pip install qrcode[pil]
```

Run the script from this folder:

```bash
python qrcode.py
```

Enter a valid UPI ID when prompted. The generated images are saved in the current working directory.

## Why a QR Scan May Not Show a Bank Name or Allow Payment

A UPI QR code encodes payment details such as the recipient's UPI ID; it does not itself specify the recipient's bank. The UPI app resolves the VPA and displays the account/payee details it can verify. A bank name may not be shown until the payment app resolves the UPI ID, and the app or bank may determine what recipient information is displayed.

The sample code uses placeholder values (`Recipient Name` and `mc=1234`) and only includes a few URI parameters. Replace placeholders with accurate recipient details. Do not invent a merchant code: use a valid merchant code only when applicable, or omit the optional parameter. Also ensure the UPI ID is correct and active, and that the payment app supports the URI. QR creation does not guarantee that a payment can be completed; test with the intended UPI app and verify the payee shown in the app before approving any payment.

For production use, construct the URI with proper URL encoding for user-provided values, validate inputs, and follow the payment provider's current UPI integration requirements. Never treat a scanned QR code as proof that a payment has succeeded.
