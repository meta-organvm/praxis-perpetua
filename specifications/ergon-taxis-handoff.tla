---------------- MODULE ergon_taxis_handoff ----------------
EXTENDS Naturals, Sequences, TLC

(*
--algorithm WebhookHandoff {
  variables 
    queue = <<>>,                 \* Simulates network payload in transit
    database = [id \in Nat |-> FALSE],  \* Taxis deduplication ledger
    webhook_sent = 0,             \* Counter for Ergon
    webhook_processed = 0;        \* Counter for Taxis

  macro SendWebhook(id) {
    queue := Append(queue, id);
    webhook_sent := webhook_sent + 1;
  }

  process (Ergon = 1) {
    \* Ergon non-deterministically sends the same webhook multiple times (network retry simulation)
    SendEvent:
      while (webhook_sent < 3) {
        either
          SendWebhook(1); \* Send the event
        or
          SendWebhook(1); \* Oh no, a timeout! Send it again to be safe.
        };
  }

  process (Taxis = 2) {
    \* Taxis constantly listens and processes
    ReceiveEvent:
      while (TRUE) {
        await Len(queue) > 0;
        with (event_id = Head(queue)) {
          queue := Tail(queue);
          
          \* The Linear Logic Idempotency check
          if (database[event_id] = FALSE) {
            database[event_id] := TRUE;
            webhook_processed := webhook_processed + 1;
          }
        }
      }
  }
}
*)

\* IDEMPOTENCY INVARIANT
\* We mathematically prove that no matter how many times Ergon retries (up to 3 in this bounded model),
\* Taxis will ONLY ever process the webhook with ID=1 exactly ONE time.
Idempotency == (webhook_processed <= 1)

\* BEGIN TRANSLATION
\* ... (TLA+ translation to be generated) ...
\* END TRANSLATION

=============================================================