#![no_std]
#![no_main]

extern crate alloc;

use alloc::vec::Vec;

use iroha_wasm::data_model::prelude::*;

#[iroha_wasm::iroha_wasm]
fn smartcontract_entry_point(_account_id: AccountId) {
    let query = QueryBox::FindAllDomains(FindAllDomains {});
    let domains: Vec<Domain> = query.execute().try_into().unwrap();

    for domain in domains {
        let new_account_id = AccountId {
            name: Name::new("mad_hatter").unwrap(),
            domain_id: domain.id,
        };

        Instruction::Register(RegisterBox::new(NewAccount::new(new_account_id))).execute();
    }
}
