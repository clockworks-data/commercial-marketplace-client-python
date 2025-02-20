# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class AadIdentifier(msrest.serialization.Model):
    """AadIdentifier.

    :param email_id:
    :type email_id: str
    :param object_id:
    :type object_id: str
    :param tenant_id:
    :type tenant_id: str
    :param puid:
    :type puid: str
    """

    _attribute_map = {
        'email_id': {'key': 'emailId', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'puid': {'key': 'puid', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AadIdentifier, self).__init__(**kwargs)
        self.email_id = kwargs.get('email_id', None)
        self.object_id = kwargs.get('object_id', None)
        self.tenant_id = kwargs.get('tenant_id', None)
        self.puid = kwargs.get('puid', None)


class FulfillmentInternalServerErrorResponse(msrest.serialization.Model):
    """FulfillmentInternalServerErrorResponse.

    :param error:
    :type error: ~microsoft.marketplace.saas.models.FulfillmentInternalServerErrorResponseError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'FulfillmentInternalServerErrorResponseError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FulfillmentInternalServerErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class FulfillmentInternalServerErrorResponseError(msrest.serialization.Model):
    """FulfillmentInternalServerErrorResponseError.

    :param code:
    :type code: str
    :param message:
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FulfillmentInternalServerErrorResponseError, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class MeteringDimension(msrest.serialization.Model):
    """MeteringDimension.

    :param id:
    :type id: str
    :param currency:
    :type currency: str
    :param price_per_unit:
    :type price_per_unit: float
    :param unit_of_measure:
    :type unit_of_measure: str
    :param display_name:
    :type display_name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'currency': {'key': 'currency', 'type': 'str'},
        'price_per_unit': {'key': 'pricePerUnit', 'type': 'float'},
        'unit_of_measure': {'key': 'unitOfMeasure', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MeteringDimension, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.currency = kwargs.get('currency', None)
        self.price_per_unit = kwargs.get('price_per_unit', None)
        self.unit_of_measure = kwargs.get('unit_of_measure', None)
        self.display_name = kwargs.get('display_name', None)


class MeteringedQuantityIncluded(msrest.serialization.Model):
    """MeteringedQuantityIncluded.

    :param dimension_id:
    :type dimension_id: str
    :param units:
    :type units: str
    """

    _attribute_map = {
        'dimension_id': {'key': 'dimensionId', 'type': 'str'},
        'units': {'key': 'units', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MeteringedQuantityIncluded, self).__init__(**kwargs)
        self.dimension_id = kwargs.get('dimension_id', None)
        self.units = kwargs.get('units', None)


class Operation(msrest.serialization.Model):
    """Operation.

    :param id:
    :type id: str
    :param activity_id:
    :type activity_id: str
    :param subscription_id:
    :type subscription_id: str
    :param offer_id:
    :type offer_id: str
    :param publisher_id:
    :type publisher_id: str
    :param plan_id:
    :type plan_id: str
    :param quantity:
    :type quantity: int
    :param action:  Possible values include: "Unsubscribe", "ChangePlan", "ChangeQuantity",
     "Suspend", "Reinstate".
    :type action: str or ~microsoft.marketplace.saas.models.OperationActionEnum
    :param time_stamp:
    :type time_stamp: ~datetime.datetime
    :param status:  Possible values include: "NotStarted", "InProgress", "Succeeded", "Failed",
     "Conflict".
    :type status: str or ~microsoft.marketplace.saas.models.OperationStatusEnum
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'activity_id': {'key': 'activityId', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'offer_id': {'key': 'offerId', 'type': 'str'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'quantity': {'key': 'quantity', 'type': 'int'},
        'action': {'key': 'action', 'type': 'str'},
        'time_stamp': {'key': 'timeStamp', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.activity_id = kwargs.get('activity_id', None)
        self.subscription_id = kwargs.get('subscription_id', None)
        self.offer_id = kwargs.get('offer_id', None)
        self.publisher_id = kwargs.get('publisher_id', None)
        self.plan_id = kwargs.get('plan_id', None)
        self.quantity = kwargs.get('quantity', None)
        self.action = kwargs.get('action', None)
        self.time_stamp = kwargs.get('time_stamp', None)
        self.status = kwargs.get('status', None)


class OperationList(msrest.serialization.Model):
    """OperationList.

    :param operations:
    :type operations: list[~microsoft.marketplace.saas.models.Operation]
    """

    _attribute_map = {
        'operations': {'key': 'operations', 'type': '[Operation]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationList, self).__init__(**kwargs)
        self.operations = kwargs.get('operations', None)


class Plan(msrest.serialization.Model):
    """Plan.

    :param plan_id:
    :type plan_id: str
    :param display_name:
    :type display_name: str
    :param is_private:
    :type is_private: bool
    :param description:
    :type description: str
    :param has_free_trials:
    :type has_free_trials: bool
    :param is_price_per_seat:
    :type is_price_per_seat: bool
    :param is_stop_sell:
    :type is_stop_sell: bool
    :param market:
    :type market: str
    :param plan_components:
    :type plan_components: ~microsoft.marketplace.saas.models.PlanComponents
    """

    _attribute_map = {
        'plan_id': {'key': 'planId', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'is_private': {'key': 'isPrivate', 'type': 'bool'},
        'description': {'key': 'description', 'type': 'str'},
        'has_free_trials': {'key': 'hasFreeTrials', 'type': 'bool'},
        'is_price_per_seat': {'key': 'isPricePerSeat', 'type': 'bool'},
        'is_stop_sell': {'key': 'isStopSell', 'type': 'bool'},
        'market': {'key': 'market', 'type': 'str'},
        'plan_components': {'key': 'planComponents', 'type': 'PlanComponents'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Plan, self).__init__(**kwargs)
        self.plan_id = kwargs.get('plan_id', None)
        self.display_name = kwargs.get('display_name', None)
        self.is_private = kwargs.get('is_private', None)
        self.description = kwargs.get('description', None)
        self.has_free_trials = kwargs.get('has_free_trials', None)
        self.is_price_per_seat = kwargs.get('is_price_per_seat', None)
        self.is_stop_sell = kwargs.get('is_stop_sell', None)
        self.market = kwargs.get('market', None)
        self.plan_components = kwargs.get('plan_components', None)


class PlanComponents(msrest.serialization.Model):
    """PlanComponents.

    :param recurrent_billing_terms:
    :type recurrent_billing_terms: list[~microsoft.marketplace.saas.models.RecurrentBillingTerm]
    :param metering_dimensions:
    :type metering_dimensions: list[~microsoft.marketplace.saas.models.MeteringDimension]
    """

    _attribute_map = {
        'recurrent_billing_terms': {'key': 'recurrentBillingTerms', 'type': '[RecurrentBillingTerm]'},
        'metering_dimensions': {'key': 'meteringDimensions', 'type': '[MeteringDimension]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PlanComponents, self).__init__(**kwargs)
        self.recurrent_billing_terms = kwargs.get('recurrent_billing_terms', None)
        self.metering_dimensions = kwargs.get('metering_dimensions', None)


class RecurrentBillingTerm(msrest.serialization.Model):
    """RecurrentBillingTerm.

    :param currency:
    :type currency: str
    :param price:
    :type price: float
    :param term_unit:  Possible values include: "P1M", "P1Y".
    :type term_unit: str or ~microsoft.marketplace.saas.models.TermUnitEnum
    :param term_description:
    :type term_description: str
    :param metered_quantity_included:
    :type metered_quantity_included:
     list[~microsoft.marketplace.saas.models.MeteringedQuantityIncluded]
    """

    _attribute_map = {
        'currency': {'key': 'currency', 'type': 'str'},
        'price': {'key': 'price', 'type': 'float'},
        'term_unit': {'key': 'termUnit', 'type': 'str'},
        'term_description': {'key': 'termDescription', 'type': 'str'},
        'metered_quantity_included': {'key': 'meteredQuantityIncluded', 'type': '[MeteringedQuantityIncluded]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RecurrentBillingTerm, self).__init__(**kwargs)
        self.currency = kwargs.get('currency', None)
        self.price = kwargs.get('price', None)
        self.term_unit = kwargs.get('term_unit', None)
        self.term_description = kwargs.get('term_description', None)
        self.metered_quantity_included = kwargs.get('metered_quantity_included', None)


class ResolvedSubscription(msrest.serialization.Model):
    """Summary of the subscription.

    :param id:
    :type id: str
    :param subscription_name:
    :type subscription_name: str
    :param offer_id:
    :type offer_id: str
    :param plan_id:
    :type plan_id: str
    :param quantity:
    :type quantity: long
    :param subscription:
    :type subscription: ~microsoft.marketplace.saas.models.Subscription
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'subscription_name': {'key': 'subscriptionName', 'type': 'str'},
        'offer_id': {'key': 'offerId', 'type': 'str'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'quantity': {'key': 'quantity', 'type': 'long'},
        'subscription': {'key': 'subscription', 'type': 'Subscription'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResolvedSubscription, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.subscription_name = kwargs.get('subscription_name', None)
        self.offer_id = kwargs.get('offer_id', None)
        self.plan_id = kwargs.get('plan_id', None)
        self.quantity = kwargs.get('quantity', None)
        self.subscription = kwargs.get('subscription', None)


class SubscriberPlan(msrest.serialization.Model):
    """SubscriberPlan.

    :param plan_id:
    :type plan_id: str
    :param quantity:
    :type quantity: long
    """

    _attribute_map = {
        'plan_id': {'key': 'planId', 'type': 'str'},
        'quantity': {'key': 'quantity', 'type': 'long'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SubscriberPlan, self).__init__(**kwargs)
        self.plan_id = kwargs.get('plan_id', None)
        self.quantity = kwargs.get('quantity', None)


class Subscription(msrest.serialization.Model):
    """Subscription.

    :param id:
    :type id: str
    :param publisher_id:
    :type publisher_id: str
    :param offer_id:
    :type offer_id: str
    :param name:
    :type name: str
    :param saas_subscription_status: Indicates the status of the operation. Possible values
     include: "NotStarted", "PendingFulfillmentStart", "Subscribed", "Suspended", "Unsubscribed".
    :type saas_subscription_status: str or
     ~microsoft.marketplace.saas.models.SubscriptionStatusEnum
    :param beneficiary:
    :type beneficiary: ~microsoft.marketplace.saas.models.AadIdentifier
    :param purchaser:
    :type purchaser: ~microsoft.marketplace.saas.models.AadIdentifier
    :param plan_id:
    :type plan_id: str
    :param quantity:
    :type quantity: int
    :param term:
    :type term: ~microsoft.marketplace.saas.models.SubscriptionTerm
    :param auto_renew: Indicating whether the subscription will renew automatically.
    :type auto_renew: bool
    :param is_test: Indicating whether the current subscription is a test asset.
    :type is_test: bool
    :param is_free_trial: true - the customer subscription is currently in free trial, false - the
     customer subscription is not currently in free trial.(optional field - default false).
    :type is_free_trial: bool
    :param allowed_customer_operations:
    :type allowed_customer_operations: list[str or
     ~microsoft.marketplace.saas.models.AllowedCustomerOperationsEnum]
    :param session_id:
    :type session_id: str
    :param fulfillment_id:
    :type fulfillment_id: str
    :param store_front:
    :type store_front: str
    :param sandbox_type: Possible Values are None, Csp (Csp sandbox purchase). Possible values
     include: "None", "Csp".
    :type sandbox_type: str or ~microsoft.marketplace.saas.models.SandboxTypeEnum
    :param created:
    :type created: ~datetime.datetime
    :param session_mode: Dry Run indicates all transactions run as Test-Mode in the commerce stack.
     Possible values include: "None", "DryRun".
    :type session_mode: str or ~microsoft.marketplace.saas.models.SessionModeEnum
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'offer_id': {'key': 'offerId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'saas_subscription_status': {'key': 'saasSubscriptionStatus', 'type': 'str'},
        'beneficiary': {'key': 'beneficiary', 'type': 'AadIdentifier'},
        'purchaser': {'key': 'purchaser', 'type': 'AadIdentifier'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'quantity': {'key': 'quantity', 'type': 'int'},
        'term': {'key': 'term', 'type': 'SubscriptionTerm'},
        'auto_renew': {'key': 'autoRenew', 'type': 'bool'},
        'is_test': {'key': 'isTest', 'type': 'bool'},
        'is_free_trial': {'key': 'isFreeTrial', 'type': 'bool'},
        'allowed_customer_operations': {'key': 'allowedCustomerOperations', 'type': '[str]'},
        'session_id': {'key': 'sessionId', 'type': 'str'},
        'fulfillment_id': {'key': 'fulfillmentId', 'type': 'str'},
        'store_front': {'key': 'storeFront', 'type': 'str'},
        'sandbox_type': {'key': 'sandboxType', 'type': 'str'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'session_mode': {'key': 'sessionMode', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Subscription, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.publisher_id = kwargs.get('publisher_id', None)
        self.offer_id = kwargs.get('offer_id', None)
        self.name = kwargs.get('name', None)
        self.saas_subscription_status = kwargs.get('saas_subscription_status', None)
        self.beneficiary = kwargs.get('beneficiary', None)
        self.purchaser = kwargs.get('purchaser', None)
        self.plan_id = kwargs.get('plan_id', None)
        self.quantity = kwargs.get('quantity', None)
        self.term = kwargs.get('term', None)
        self.auto_renew = kwargs.get('auto_renew', None)
        self.is_test = kwargs.get('is_test', None)
        self.is_free_trial = kwargs.get('is_free_trial', None)
        self.allowed_customer_operations = kwargs.get('allowed_customer_operations', None)
        self.session_id = kwargs.get('session_id', None)
        self.fulfillment_id = kwargs.get('fulfillment_id', None)
        self.store_front = kwargs.get('store_front', None)
        self.sandbox_type = kwargs.get('sandbox_type', None)
        self.created = kwargs.get('created', None)
        self.session_mode = kwargs.get('session_mode', None)


class SubscriptionPlans(msrest.serialization.Model):
    """SubscriptionPlans.

    :param plans:
    :type plans: list[~microsoft.marketplace.saas.models.Plan]
    """

    _attribute_map = {
        'plans': {'key': 'plans', 'type': '[Plan]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SubscriptionPlans, self).__init__(**kwargs)
        self.plans = kwargs.get('plans', None)


class SubscriptionsResponse(msrest.serialization.Model):
    """SubscriptionsResponse.

    :param subscriptions:
    :type subscriptions: list[~microsoft.marketplace.saas.models.Subscription]
    :param next_link: Link to get the next set of subscriptions.
    :type next_link: str
    """

    _attribute_map = {
        'subscriptions': {'key': 'subscriptions', 'type': '[Subscription]'},
        'next_link': {'key': '@nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SubscriptionsResponse, self).__init__(**kwargs)
        self.subscriptions = kwargs.get('subscriptions', None)
        self.next_link = kwargs.get('next_link', None)


class SubscriptionTerm(msrest.serialization.Model):
    """SubscriptionTerm.

    :param start_date:
    :type start_date: ~datetime.datetime
    :param end_date:
    :type end_date: ~datetime.datetime
    :param term_unit:
    :type term_unit: str
    """

    _attribute_map = {
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'term_unit': {'key': 'termUnit', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SubscriptionTerm, self).__init__(**kwargs)
        self.start_date = kwargs.get('start_date', None)
        self.end_date = kwargs.get('end_date', None)
        self.term_unit = kwargs.get('term_unit', None)


class UpdateOperation(msrest.serialization.Model):
    """UpdateOperation.

    :param plan_id:
    :type plan_id: str
    :param quantity:
    :type quantity: long
    :param status:  Possible values include: "Success", "Failure".
    :type status: str or ~microsoft.marketplace.saas.models.UpdateOperationStatusEnum
    """

    _attribute_map = {
        'plan_id': {'key': 'planId', 'type': 'str'},
        'quantity': {'key': 'quantity', 'type': 'long'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(UpdateOperation, self).__init__(**kwargs)
        self.plan_id = kwargs.get('plan_id', None)
        self.quantity = kwargs.get('quantity', None)
        self.status = kwargs.get('status', None)
