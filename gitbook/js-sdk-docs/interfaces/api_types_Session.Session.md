[@julep/sdk](../README.md) / [Modules](../modules.md) / [api/types/Session](../modules/api_types_Session.md) / Session

# Interface: Session

[api/types/Session](../modules/api_types_Session.md).Session

This file was auto-generated by Fern from our API Definition.

## Table of contents

### Properties

- [agentId](api_types_Session.Session.md#agentid)
- [createdAt](api_types_Session.Session.md#createdat)
- [id](api_types_Session.Session.md#id)
- [situation](api_types_Session.Session.md#situation)
- [summary](api_types_Session.Session.md#summary)
- [updatedAt](api_types_Session.Session.md#updatedat)
- [userId](api_types_Session.Session.md#userid)

## Properties

### agentId

• **agentId**: `string`

Agent ID of agent associated with this session

#### Defined in

[src/api/api/types/Session.d.ts:10](https://github.com/julep-ai/samantha-monorepo/blob/9aefd53/sdks/js/src/api/api/types/Session.d.ts#L10)

___

### createdAt

• `Optional` **createdAt**: `Date`

Session created at (RFC-3339 format)

#### Defined in

[src/api/api/types/Session.d.ts:16](https://github.com/julep-ai/samantha-monorepo/blob/9aefd53/sdks/js/src/api/api/types/Session.d.ts#L16)

___

### id

• **id**: `string`

Session id (UUID)

#### Defined in

[src/api/api/types/Session.d.ts:6](https://github.com/julep-ai/samantha-monorepo/blob/9aefd53/sdks/js/src/api/api/types/Session.d.ts#L6)

___

### situation

• `Optional` **situation**: `string`

A specific situation that sets the background for this session

#### Defined in

[src/api/api/types/Session.d.ts:12](https://github.com/julep-ai/samantha-monorepo/blob/9aefd53/sdks/js/src/api/api/types/Session.d.ts#L12)

___

### summary

• `Optional` **summary**: `string`

(null at the beginning) - generated automatically after every interaction

#### Defined in

[src/api/api/types/Session.d.ts:14](https://github.com/julep-ai/samantha-monorepo/blob/9aefd53/sdks/js/src/api/api/types/Session.d.ts#L14)

___

### updatedAt

• `Optional` **updatedAt**: `Date`

Session updated at (RFC-3339 format)

#### Defined in

[src/api/api/types/Session.d.ts:18](https://github.com/julep-ai/samantha-monorepo/blob/9aefd53/sdks/js/src/api/api/types/Session.d.ts#L18)

___

### userId

• **userId**: `string`

User ID of user associated with this session

#### Defined in

[src/api/api/types/Session.d.ts:8](https://github.com/julep-ai/samantha-monorepo/blob/9aefd53/sdks/js/src/api/api/types/Session.d.ts#L8)